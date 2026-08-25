#!/usr/bin/env python3
"""Dependency-free structural validation for the architecture-docs package."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]
REQUIRED = {
    ROOT / "docs" / "architecture.md": ["## Purpose", "## Architectural principles", "## Integration checklist", "## Non-claims"],
    ROOT / "docs" / "adr-template.md": ["## Status", "## Context", "## Decision", "## Alternatives considered", "## Consequences", "## Verification", "## Rollback / supersession"],
}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def validate() -> list[str]:
    errors: list[str] = []
    for path in DOCS:
        if not path.exists():
            errors.append(f"missing document: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("# "):
            errors.append(f"{path.relative_to(ROOT)} must begin with an H1")
        if len(text.encode("utf-8")) > 128 * 1024:
            errors.append(f"{path.relative_to(ROOT)} exceeds 128 KiB")

        for raw_link in LINK_RE.findall(text):
            if raw_link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = raw_link.split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)} link escapes repository: {raw_link}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)} has missing local link: {raw_link}")

    for path, headings in REQUIRED.items():
        if not path.exists():
            errors.append(f"missing required document: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                errors.append(f"{path.relative_to(ROOT)} missing heading: {heading}")

    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        raise SystemExit(1)
    print(f"validated {len(DOCS)} markdown documents")
