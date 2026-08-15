#!/usr/bin/env python3
"""Snabb validering för Kvartalsmötet i GitHub Actions.

Validerar den kanoniska projektstrukturen, metadata, omslag, kapitelserie,
rubrikformat och interna Markdown-länkar med enbart Python-standardbiblioteket.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

CHAPTER_RE = re.compile(r"kapitel-(\d{2,})\.md$")
CHAPTER_H1_RE = re.compile(r"^#\s+Kapitel\s+(\d+)\s+[–-]\s+(.+?)\s*$")
MARKERS = ("TODO", "FIXME", "[PLACEHOLDER]")

REQUIRED_PATHS = (
    "README.md",
    "project-manifest.json",
    "roman-bibel.md",
    "synopsis.md",
    "kapitelplan.md",
    "projektstatus.md",
    "project-index.md",
    "kapitel",
    "omslag/omslag-kvartalsmotet.png",
    "publishing/metadata.yaml",
    "publishing/epub.css",
    "publishing/fix-epub-after-pandoc.py",
    "publishing/pdf-template.tex",
    "publishing/pdf-filter.lua",
    "scripts/build_book.py",
)

REQUIRED_METADATA_KEYS = ("title", "author", "language", "cover-image")

def error(errors: list[str], message: str) -> None:
    errors.append(message)
    print(f"ERROR: {message}", file=sys.stderr)

def parse_simple_yaml_scalars(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key or key.startswith("-"):
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key] = value
    return values

def validate_markdown_links(root: Path, errors: list[str]) -> None:
    link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for md in sorted(root.rglob("*.md")):
        if any(part in {".git", ".github"} for part in md.relative_to(root).parts):
            continue
        text = md.read_text(encoding="utf-8")
        for target in link_re.findall(text):
            target = target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            if " " in target and not target.startswith(("./", "../")):
                target = target.split(" ", 1)[0]
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                continue
            if not candidate.exists():
                error(errors, f"Trasig intern Markdown-länk i {md.relative_to(root)}: {target}")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors: list[str] = []

    if not root.is_dir():
        error(errors, f"Projektkatalogen finns inte: {root}")
        return 1

    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            error(errors, f"Obligatorisk projektsökväg saknas: {rel}")

    if errors:
        return 1

    try:
        manifest = json.loads((root / "project-manifest.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        error(errors, f"project-manifest.json är ogiltig: {exc}")
        return 1

    chapter_dir = root / "kapitel"
    canonical: dict[int, Path] = {}
    alternatives: list[str] = []
    for path in sorted(chapter_dir.iterdir()):
        if not path.is_file():
            continue
        match = CHAPTER_RE.fullmatch(path.name)
        if match:
            number = int(match.group(1))
            if number in canonical:
                error(errors, f"Två filer representerar kapitel {number}.")
            canonical[number] = path
        elif path.name.lower() != "kapitelmall.md" and re.search(r"kapitel.*\d", path.name, re.I):
            alternatives.append(path.name)

    if alternatives:
        error(errors, "Icke-kanoniska möjliga kapitelfiler hittades: " + ", ".join(alternatives))

    numbers = sorted(canonical)
    if not numbers:
        error(errors, "Inga kapitel hittades.")
    else:
        expected = list(range(1, numbers[-1] + 1))
        missing = sorted(set(expected) - set(numbers))
        if missing:
            error(errors, "Kapitel saknas: " + ", ".join(map(str, missing)))

    manifest_chapters = manifest.get("chapters", {})
    if manifest_chapters.get("count") != len(numbers):
        error(errors, f"Manifestets kapitelantal ({manifest_chapters.get('count')}) matchar inte filerna ({len(numbers)}).")
    if numbers and manifest_chapters.get("latest") != numbers[-1]:
        error(errors, f"Manifestets senaste kapitel ({manifest_chapters.get('latest')}) matchar inte filerna ({numbers[-1]}).")

    for number, path in sorted(canonical.items()):
        text = path.read_text(encoding="utf-8")
        stripped = text.strip()
        if not stripped:
            error(errors, f"{path.relative_to(root)} är tom.")
            continue
        first_line = stripped.splitlines()[0].strip()
        match = CHAPTER_H1_RE.fullmatch(first_line)
        if not match:
            error(errors, f"{path.relative_to(root)} har fel H1-format; väntat '# Kapitel {number} – Titel'.")
        elif int(match.group(1)) != number:
            error(errors, f"{path.relative_to(root)} har kapitelnummer {match.group(1)} i H1.")
        for marker in MARKERS:
            if marker in text:
                error(errors, f"{path.relative_to(root)} innehåller arbetsmarkören {marker}.")

    metadata = parse_simple_yaml_scalars(root / "publishing/metadata.yaml")
    for key in REQUIRED_METADATA_KEYS:
        if not metadata.get(key):
            error(errors, f"publishing/metadata.yaml saknar värde för '{key}'.")
    if metadata.get("title") != "Kvartalsmötet":
        error(errors, "Metadatafältet title matchar inte projektets fastställda titel.")
    if metadata.get("subtitle") != "Protokollet var redan skrivet":
        error(errors, "Metadatafältet subtitle matchar inte projektets fastställda undertitel.")
    if metadata.get("author") != "Erland Lindmark":
        error(errors, "Metadatafältet author matchar inte projektets fastställda författare.")
    cover_rel = metadata.get("cover-image", "")
    if cover_rel and not (root / cover_rel).exists():
        error(errors, f"Metadatafältet cover-image pekar på saknad fil: {cover_rel}")

    validate_markdown_links(root, errors)

    if errors:
        print(f"\nValidation failed: {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"OK: projektvalidering godkänd. Revision {manifest.get('revision')}, {len(numbers)} kapitel.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
