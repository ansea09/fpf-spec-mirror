#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_PATTERNS = [
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
    "C.7",
    "C.24",
    "C.27",
    "C.28",
    "E.17",
    "E.17.EFP",
    "G.6",
    "G.11",
]

REQUIRED_FRONT_MATTER_KEYS = [
    "chunk_kind",
    "pattern_id",
    "pattern_title",
    "source_path",
    "output_path",
    "commit_sha",
    "heading_path",
    "line_start",
    "line_end",
    "dependencies",
    "keywords",
]


def read_front_matter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")

    if not text.startswith("---\n"):
        raise AssertionError(f"{path}: missing front matter")

    end = text.find("\n---\n", 4)
    if end == -1:
        raise AssertionError(f"{path}: malformed front matter")

    return text[4:end]


def extract_scalar_int(front_matter: str, key: str) -> int:
    prefix = f"{key}:"
    for line in front_matter.splitlines():
        if line.startswith(prefix):
            value = line.split(":", 1)[1].strip()
            return int(value)
    raise AssertionError(f"Missing integer key: {key}")


def validate_front_matter(path: Path, total_source_lines: int) -> None:
    fm = read_front_matter(path)

    for key in REQUIRED_FRONT_MATTER_KEYS:
        if f"{key}:" not in fm:
            raise AssertionError(f"{path}: missing metadata key {key}")

    line_start = extract_scalar_int(fm, "line_start")
    line_end = extract_scalar_int(fm, "line_end")

    if line_start < 1:
        raise AssertionError(f"{path}: line_start must be >= 1")

    if line_end < line_start:
        raise AssertionError(f"{path}: line_end must be >= line_start")

    if line_end > total_source_lines:
        raise AssertionError(
            f"{path}: line_end {line_end} exceeds source line count {total_source_lines}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate generated FPF pattern-aware chunks"
    )
    parser.add_argument("--source", default="FPF-Spec.md")
    parser.add_argument("--chunks", default="fpf_chunks")
    args = parser.parse_args()

    source = Path(args.source)
    chunks = Path(args.chunks)

    if not source.exists():
        raise SystemExit(f"Source file not found: {source}")

    if not chunks.exists():
        raise SystemExit(f"Chunks directory not found: {chunks}")

    manifest_path = chunks / "manifest.json"
    metadata_path = chunks / "metadata.jsonl"
    index_path = chunks / "000-index.md"

    if not manifest_path.exists():
        raise SystemExit("Missing fpf_chunks/manifest.json")

    if not metadata_path.exists():
        raise SystemExit("Missing fpf_chunks/metadata.jsonl")

    if not index_path.exists():
        raise SystemExit("Missing fpf_chunks/000-index.md")

    by_pattern = chunks / "by_pattern"
    by_section = chunks / "by_section"

    if not by_pattern.exists():
        raise SystemExit("Missing fpf_chunks/by_pattern")

    if not by_section.exists():
        raise SystemExit("Missing fpf_chunks/by_section")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    patterns = manifest.get("patterns", [])

    if not patterns:
        raise SystemExit("Manifest contains no patterns")

    pattern_ids = {item["pattern_id"] for item in patterns}

    missing = [pattern_id for pattern_id in REQUIRED_PATTERNS if pattern_id not in pattern_ids]
    if missing:
        raise SystemExit(
            "Required FPF patterns were not found in generated chunks: "
            + ", ".join(missing)
        )

    source_line_count = len(source.read_text(encoding="utf-8").splitlines())

    parent_files = sorted(by_pattern.glob("*.md"))
    child_files = sorted(by_section.glob("**/*.md"))

    if not parent_files:
        raise SystemExit("No parent chunks found in fpf_chunks/by_pattern")

    if not child_files:
        raise SystemExit("No child chunks found in fpf_chunks/by_section")

    for item in patterns:
        parent = chunks / item["parent_chunk"]
        if not parent.exists():
            raise SystemExit(f"Missing parent chunk: {parent}")

        child_chunks = item.get("child_chunks", [])
        if not child_chunks:
            raise SystemExit(f"Pattern {item['pattern_id']} has no child chunks")

        for rel in child_chunks:
            child = chunks / rel
            if not child.exists():
                raise SystemExit(f"Missing child chunk: {child}")

    for path in parent_files + child_files:
        validate_front_matter(path, source_line_count)

    old_part_files = list(chunks.glob("*-FPF-Spec.part.md"))
    if old_part_files:
        raise SystemExit(
            "Old byte-based part files still exist: "
            + ", ".join(str(p) for p in old_part_files[:10])
        )

    print(
        f"OK: validated {len(parent_files)} parent chunks, "
        f"{len(child_files)} child chunks, {len(patterns)} patterns"
    )


if __name__ == "__main__":
    main()
