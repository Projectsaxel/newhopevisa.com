#!/usr/bin/env python3
"""Converte asset.css?ver=X → asset﹖ver=X.css (nomes do espelho HTTrack)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIRROR_Q = "\uFE56"
PATTERN = re.compile(
	r"([\"'])([^\"']+?)\.(css|js)\?ver=([^\"'&\s]+)\1",
	re.IGNORECASE,
)


def fix_url(match: re.Match[str]) -> str:
	quote, base, ext, ver = match.groups()
	return f"{quote}{base}{MIRROR_Q}ver={ver}.{ext}{quote}"


def main() -> None:
	updated = 0
	refs = 0
	for html in sorted(ROOT.rglob("*.html")):
		if "scripts" in html.parts:
			continue
		text = html.read_text(encoding="utf-8")
		new_text, count = PATTERN.subn(fix_url, text)
		if count:
			html.write_text(new_text, encoding="utf-8")
			updated += 1
			refs += count
	print(f"Arquivos HTML: {updated}, referências corrigidas: {refs}")


if __name__ == "__main__":
	main()
