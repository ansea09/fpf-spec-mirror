#!/usr/bin/env python3
from pathlib import Path

SRC = Path("FPF-Spec.md")
OUT_DIR = Path("fpf_chunks")
MAX_BYTES = 240 * 1024  # запас, чтобы гарантированно быть < 350 KiB

def main():
    text = SRC.read_text(encoding="utf-8", errors="strict").splitlines(keepends=True)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # очистим старые чанки (кроме README/INDEX если захотите)
    for p in OUT_DIR.glob("*.md"):
        p.unlink()

    part = 1
    buf = []
    buf_bytes = 0

    def flush():
        nonlocal part, buf, buf_bytes
        if not buf:
            return
        out = OUT_DIR / f"{part:03d}-FPF-Spec.part.md"
        out.write_text("".join(buf), encoding="utf-8")
        part += 1
        buf = []
        buf_bytes = 0

    for line in text:
        b = len(line.encode("utf-8"))
        # если одна строка сама по себе огромная — всё равно кладём, но это риск для Code Search
        if buf and (buf_bytes + b) > MAX_BYTES:
            flush()
        buf.append(line)
        buf_bytes += b

    flush()

    # индекс/оглавление
    index = OUT_DIR / "000-index.md"
    parts = sorted([p.name for p in OUT_DIR.glob("*.md") if p.name != "000-index.md"])
    index_lines = [
        "# FPF chunks index\n",
        "\n",
        "Автосгенерированные части файла `FPF-Spec.md` (для поиска и RAG).\n",
        "\n",
        "## Parts\n",
        "\n",
    ]
    for name in parts:
        index_lines.append(f"- [{name}]({name})\n")
    index.write_text("".join(index_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
