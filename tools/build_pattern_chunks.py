#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


PATTERN_ID_RE = re.compile(
    r"^(?:[A-Z](?:\.[A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*)+|G\.Core)$"
)

ANY_PATTERN_ID_RE = re.compile(
    r"\b(?:[A-Z](?:\.[A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*)+|G\.Core)\b"
)

PATTERN_HEADING_RE = re.compile(
    r"^##\s+"
    r"(?P<id>(?:[A-Z](?:\.[A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*)+|G\.Core))"
    r"\s*(?:[-–—:]\s*)?"
    r"(?P<title>.*)"
    r"$"
)

SECTION_HEADING_RE = re.compile(r"^###\s+(?P<title>.+?)\s*$")

DEPENDENCY_LABELS = (
    "Builds on",
    "Builds / Grounds",
    "Coordinates with",
    "Depends on",
    "Prerequisite for",
    "Used by",
    "Uses",
    "Constrains",
    "Constrained by",
    "Relates to",
    "Interacts with",
    "Informs",
    "Enables",
    "Refines",
    "Specialised by",
    "Specialized by",
)

CHR_CAL_REPLACEMENT_PATTERNS = [
    # C.7 CHR-CAL was deprecated/removed upstream. The required contract now
    # validates the existing replacement basis instead of a removed ToC entry.
    "A.17",
    "A.18",
    "A.19",
    "C.16",
    "G.3",
    "G.4",
]

DEPRECATED_PATTERN_MIGRATIONS = {
    "C.7": {
        "status": "deprecated_or_removed",
        "replacement_basis": CHR_CAL_REPLACEMENT_PATTERNS,
        "note": (
            "C.7 CHR-CAL is no longer required as a standalone pattern. "
            "Validate the characteristic/measurement/calculus basis through "
            "C.16 plus A.17/A.18/A.19 and G.3/G.4."
        ),
    }
}

DEFAULT_REQUIRED_PATTERNS = [
    "A.1",
    "A.1.1",
    "A.2",
    "A.2.1",
    "A.2.2",
    "A.2.4",
    "A.2.6",
    "A.3.1",
    "A.3.3",
    "A.4",
    "A.6",
    "A.6.P",
    "A.7",
    "A.10",
    "A.11",
    "A.15",
    *CHR_CAL_REPLACEMENT_PATTERNS,
    "C.24",
    "C.27",
    "C.28",
    "E.17",
    "E.17.EFP",
    "G.6",
    "G.11",
]


@dataclass
class TocMeta:
    pattern_id: str
    pattern_title: str | None
    keywords: list[str]
    dependencies: list[str]


@dataclass
class PatternBlock:
    pattern_id: str
    title: str
    start_line: int
    end_line: int
    lines: list[str]


@dataclass
class SectionBlock:
    section_id: str
    title: str
    start_line: int
    end_line: int
    lines: list[str]


@dataclass
class ChunkMeta:
    chunk_kind: str
    pattern_id: str
    pattern_title: str
    section_id: str | None
    section_title: str | None
    source_path: str
    output_path: str
    commit_sha: str
    heading_path: list[str]
    line_start: int
    line_end: int
    dependencies: list[str]
    keywords: list[str]


def strip_markdown(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = text.replace("`", "")
    return text.strip()


def slug(text: str) -> str:
    text = strip_markdown(text).lower()
    text = re.sub(r"[^a-z0-9а-яё]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "section"


def safe_id(pattern_id: str) -> str:
    return pattern_id.replace("/", "_")


def extract_ids(text: str) -> list[str]:
    return sorted(set(ANY_PATTERN_ID_RE.findall(text)))


def parse_toc_metadata(lines: list[str]) -> dict[str, TocMeta]:
    """
    Reads Table of Content rows like:
    | A.1 | **Title** | Stable | *Keywords:* ... | **Builds on:** ... |
    """
    result: dict[str, TocMeta] = {}

    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue

        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 5:
            continue

        pattern_id = strip_markdown(cells[0])
        if not PATTERN_ID_RE.match(pattern_id):
            continue

        title = strip_markdown(cells[1])
        keywords_cell = cells[3]
        deps_cell = cells[4]

        keywords: list[str] = []
        m = re.search(
            r"Keywords:\s*(.*?)(?:Queries:|$)",
            strip_markdown(keywords_cell),
            flags=re.IGNORECASE,
        )
        if m:
            raw_keywords = m.group(1)
            keywords = [
                kw.strip(" .:-")
                for kw in re.split(r"[,;]", raw_keywords)
                if kw.strip(" .:-")
            ]

        dependencies = extract_ids(strip_markdown(deps_cell))

        result[pattern_id] = TocMeta(
            pattern_id=pattern_id,
            pattern_title=title or None,
            keywords=keywords,
            dependencies=dependencies,
        )

    return result


def parse_patterns(lines: list[str], toc_meta: dict[str, TocMeta]) -> tuple[list[str], list[PatternBlock]]:
    matches: list[tuple[int, re.Match[str]]] = []

    for idx, line in enumerate(lines, start=1):
        match = PATTERN_HEADING_RE.match(line)
        if match:
            matches.append((idx, match))

    preface_end = matches[0][0] - 1 if matches else len(lines)
    preface_lines = lines[:preface_end]

    patterns: list[PatternBlock] = []

    for i, (start_line, match) in enumerate(matches):
        pattern_id = match.group("id").strip()
        heading_title = strip_markdown(match.group("title"))
        fallback_title = toc_meta.get(pattern_id).pattern_title if pattern_id in toc_meta else None
        title = heading_title or fallback_title or pattern_id

        end_line = matches[i + 1][0] - 1 if i + 1 < len(matches) else len(lines)
        block_lines = lines[start_line - 1 : end_line]

        patterns.append(
            PatternBlock(
                pattern_id=pattern_id,
                title=title,
                start_line=start_line,
                end_line=end_line,
                lines=block_lines,
            )
        )

    return preface_lines, patterns


def section_id_and_title(pattern_id: str, raw_title: str, seq: int) -> tuple[str, str]:
    raw_title = strip_markdown(raw_title)

    # Existing canonical section ids, for example:
    # A.1:1 - Problem Frame
    # A.0:QF.2a - Support-stack reading glosses
    canonical = re.match(
        rf"^(?P<section_id>{re.escape(pattern_id)}(?::[A-Za-z0-9_.-]+)?)"
        rf"\s*(?:[-–—:]\s*)?"
        rf"(?P<title>.*)$",
        raw_title,
    )

    if canonical:
        section_id = canonical.group("section_id")
        title = canonical.group("title").strip() or raw_title
        return section_id, title

    # Non-canonical headings, for example:
    # 1) Problem frame
    # 4) Solution — ...
    return f"{pattern_id}:section-{seq:03d}", raw_title


def parse_sections(pattern: PatternBlock) -> list[SectionBlock]:
    matches: list[tuple[int, int, re.Match[str]]] = []

    for offset, line in enumerate(pattern.lines):
        match = SECTION_HEADING_RE.match(line)
        if match:
            source_line = pattern.start_line + offset
            matches.append((offset, source_line, match))

    sections: list[SectionBlock] = []

    # Material between pattern heading and first ### heading.
    if matches:
        first_offset, first_source_line, _ = matches[0]
        if first_offset > 1:
            intro_lines = pattern.lines[:first_offset]
            sections.append(
                SectionBlock(
                    section_id=f"{pattern.pattern_id}:intro",
                    title="Intro",
                    start_line=pattern.start_line,
                    end_line=first_source_line - 1,
                    lines=intro_lines,
                )
            )
    else:
        return [
            SectionBlock(
                section_id=f"{pattern.pattern_id}:body",
                title="Body",
                start_line=pattern.start_line,
                end_line=pattern.end_line,
                lines=pattern.lines,
            )
        ]

    for i, (offset, source_line, match) in enumerate(matches, start=1):
        next_offset = matches[i][0] if i < len(matches) else len(pattern.lines)
        end_line = pattern.start_line + next_offset - 1

        section_id, title = section_id_and_title(
            pattern_id=pattern.pattern_id,
            raw_title=match.group("title"),
            seq=i,
        )

        sections.append(
            SectionBlock(
                section_id=section_id,
                title=title,
                start_line=source_line,
                end_line=end_line,
                lines=pattern.lines[offset:next_offset],
            )
        )

    return sections


def extract_dependencies_from_pattern(text: str) -> list[str]:
    found: set[str] = set()

    for line in text.splitlines():
        if any(label in line for label in DEPENDENCY_LABELS):
            for item in ANY_PATTERN_ID_RE.findall(line):
                found.add(item)

    return sorted(found)


def extract_keywords_from_pattern(text: str) -> list[str]:
    keywords: set[str] = set()

    for line in text.splitlines():
        if "keywords" not in line.lower():
            continue

        clean = strip_markdown(line)
        clean = re.sub(r"^.*keywords\s*:?", "", clean, flags=re.IGNORECASE)

        for part in re.split(r"[,;|]", clean):
            value = part.strip(" .:-")
            if value and len(value) <= 100:
                keywords.add(value)

    return sorted(keywords)


def merge_unique(*items: Iterable[str]) -> list[str]:
    merged: set[str] = set()
    for group in items:
        for item in group:
            value = item.strip()
            if value:
                merged.add(value)
    return sorted(merged)


def front_matter(meta: ChunkMeta) -> str:
    data = asdict(meta)
    lines = ["---\n"]

    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:\n")
            for item in value:
                lines.append(f"  - {json.dumps(item, ensure_ascii=False)}\n")
        elif value is None:
            lines.append(f"{key}: null\n")
        else:
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}\n")

    lines.append("---\n\n")
    return "".join(lines)


def write_chunk(path: Path, meta: ChunkMeta, body_lines: Iterable[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(front_matter(meta) + "".join(body_lines), encoding="utf-8")


def build(source: Path, out_dir: Path, commit_sha: str) -> None:
    if not source.exists():
        raise FileNotFoundError(f"Source file not found: {source}")

    lines = source.read_text(encoding="utf-8").splitlines(keepends=True)
    toc_meta = parse_toc_metadata(lines)
    preface_lines, patterns = parse_patterns(lines, toc_meta)

    if not patterns:
        raise RuntimeError("No FPF pattern headings found. Expected headings like '## A.1 - ...'.")

    if out_dir.exists():
        shutil.rmtree(out_dir)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "by_pattern").mkdir(parents=True, exist_ok=True)
    (out_dir / "by_section").mkdir(parents=True, exist_ok=True)
    (out_dir / "non_patterns").mkdir(parents=True, exist_ok=True)

    (out_dir / "non_patterns" / "000-preface-and-toc.md").write_text(
        "".join(preface_lines),
        encoding="utf-8",
    )

    manifest: dict[str, object] = {
        "source_path": str(source),
        "commit_sha": commit_sha,
        "chunking_method": "pattern-aware",
        "pattern_count": len(patterns),
        "deprecated_pattern_migrations": DEPRECATED_PATTERN_MIGRATIONS,
        "patterns": [],
    }

    metadata_rows: list[str] = []

    for pattern in patterns:
        pattern_text = "".join(pattern.lines)
        toc = toc_meta.get(pattern.pattern_id)

        dependencies = merge_unique(
            toc.dependencies if toc else [],
            extract_dependencies_from_pattern(pattern_text),
        )
        keywords = merge_unique(
            toc.keywords if toc else [],
            extract_keywords_from_pattern(pattern_text),
        )

        parent_rel = Path("by_pattern") / f"{safe_id(pattern.pattern_id)}.md"
        parent_path = out_dir / parent_rel

        parent_meta = ChunkMeta(
            chunk_kind="parent",
            pattern_id=pattern.pattern_id,
            pattern_title=pattern.title,
            section_id=None,
            section_title=None,
            source_path=str(source),
            output_path=str(parent_rel),
            commit_sha=commit_sha,
            heading_path=[f"{pattern.pattern_id} — {pattern.title}"],
            line_start=pattern.start_line,
            line_end=pattern.end_line,
            dependencies=dependencies,
            keywords=keywords,
        )

        write_chunk(parent_path, parent_meta, pattern.lines)
        metadata_rows.append(json.dumps(asdict(parent_meta), ensure_ascii=False))

        sections = parse_sections(pattern)
        child_paths: list[str] = []

        for idx, section in enumerate(sections, start=1):
            child_rel = (
                Path("by_section")
                / safe_id(pattern.pattern_id)
                / f"{safe_id(pattern.pattern_id)}__{idx:03d}_{slug(section.title)}.md"
            )
            child_path = out_dir / child_rel

            child_meta = ChunkMeta(
                chunk_kind="child",
                pattern_id=pattern.pattern_id,
                pattern_title=pattern.title,
                section_id=section.section_id,
                section_title=section.title,
                source_path=str(source),
                output_path=str(child_rel),
                commit_sha=commit_sha,
                heading_path=[
                    f"{pattern.pattern_id} — {pattern.title}",
                    f"{section.section_id} — {section.title}",
                ],
                line_start=section.start_line,
                line_end=section.end_line,
                dependencies=dependencies,
                keywords=keywords,
            )

            write_chunk(child_path, child_meta, section.lines)
            metadata_rows.append(json.dumps(asdict(child_meta), ensure_ascii=False))
            child_paths.append(str(child_rel))

        manifest["patterns"].append(
            {
                "pattern_id": pattern.pattern_id,
                "pattern_title": pattern.title,
                "line_start": pattern.start_line,
                "line_end": pattern.end_line,
                "parent_chunk": str(parent_rel),
                "child_chunks": child_paths,
                "dependencies": dependencies,
                "keywords": keywords,
            }
        )

    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    (out_dir / "metadata.jsonl").write_text(
        "\n".join(metadata_rows) + "\n",
        encoding="utf-8",
    )

    index_lines = [
        "# FPF pattern-aware chunks index\n\n",
        f"Source: `{source}`\n\n",
        f"Commit SHA: `{commit_sha}`\n\n",
        f"Chunking method: `pattern-aware`\n\n",
        f"Patterns: `{len(patterns)}`\n\n",
        "## Patterns\n\n",
    ]

    for item in manifest["patterns"]:
        index_lines.append(
            f"- [{item['pattern_id']} — {item['pattern_title']}]({item['parent_chunk']})\n"
        )

    (out_dir / "000-index.md").write_text("".join(index_lines), encoding="utf-8")

    missing_required = [
        pattern_id
        for pattern_id in DEFAULT_REQUIRED_PATTERNS
        if pattern_id not in {p.pattern_id for p in patterns}
    ]

    if missing_required:
        print("WARNING: Some expected FPF patterns were not found:")
        for pattern_id in missing_required:
            print(f"  - {pattern_id}")

    print(f"Built {len(patterns)} parent pattern chunks in {out_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build pattern-aware chunks for FPF-Spec.md"
    )
    parser.add_argument("--source", default="FPF-Spec.md")
    parser.add_argument("--out", default="fpf_chunks")
    parser.add_argument("--commit-sha", required=True)
    args = parser.parse_args()

    build(
        source=Path(args.source),
        out_dir=Path(args.out),
        commit_sha=args.commit_sha,
    )


if __name__ == "__main__":
    main()
