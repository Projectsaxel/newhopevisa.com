#!/usr/bin/env python3
"""Remove a extensão .html dos links internos de páginas."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# index.html como segmento de caminho → diretório/
INDEX_SEGMENT = re.compile(r"/index\.html(?=[/?#\"'&\s]|$)")

# index.html isolado em atributos / JSON de páginas
INDEX_ALONE = re.compile(
	r'(?<=["\'\s:(=])index\.html(?=[?"\'#&\s,}]|$)',
)

# API WordPress espelhada com index.html indevido
WP_JSON_PAGE = re.compile(
	r"(wp-json/wp/v2/pages/\d+)/index\.html",
)


def strip_html_extensions(text: str) -> str:
	text = WP_JSON_PAGE.sub(r"\1.json", text)
	text = INDEX_SEGMENT.sub("/", text)
	text = INDEX_ALONE.sub("./", text)
	return text


def process_file(path: Path) -> bool:
	original = path.read_text(encoding="utf-8")
	updated = strip_html_extensions(original)
	if updated == original:
		return False
	path.write_text(updated, encoding="utf-8")
	return True


def main() -> None:
	changed = 0
	for path in ROOT.rglob("*.html"):
		if "scripts" in path.parts:
			continue
		if process_file(path):
			changed += 1

	remaining = 0
	for path in ROOT.rglob("*.html"):
		if "scripts" in path.parts:
			continue
		text = path.read_text(encoding="utf-8")
		remaining += len(re.findall(r'href=["\'][^"\']*\.html', text))

	print(f"Arquivos alterados: {changed}")
	print(f"Links href com .html restantes: {remaining}")


if __name__ == "__main__":
	main()
