#!/usr/bin/env python3
"""Corrige href=\"/\" em subpastas e injeta redirecionamento anti index.html."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REDIRECT = (
	'<script src="/local-redirect.js" id="local-url-clean"></script>\n</head>'
)
LANG_DIRS = {"pt-br", "en", "es"}


def fix_root_slashes(path: Path, text: str) -> str:
	parts = path.relative_to(ROOT).parts
	if not parts or parts == ("index.html",):
		return text
	# Dentro de idioma ou subpágina: "/" aponta para raiz errada
	if parts[0] in LANG_DIRS or (len(parts) > 1 and parts[0] in LANG_DIRS):
		text = text.replace('href="/"', 'href="./"')
		text = text.replace('content="/"', 'content="./"')
		text = text.replace("href='/'", "href='./'")
		text = text.replace("content='/'", "content='./'")
	return text


def inject_redirect(text: str) -> str:
	if 'id="local-url-clean"' in text:
		return text
	if "</head>" in text:
		return text.replace("</head>", REDIRECT, 1)
	return text


def main() -> None:
	changed = 0
	for path in ROOT.rglob("*.html"):
		if "scripts" in path.parts:
			continue
		original = path.read_text(encoding="utf-8")
		updated = fix_root_slashes(path, original)
		updated = inject_redirect(updated)
		if updated != original:
			path.write_text(updated, encoding="utf-8")
			changed += 1
	print(f"Arquivos atualizados: {changed}")


if __name__ == "__main__":
	main()
