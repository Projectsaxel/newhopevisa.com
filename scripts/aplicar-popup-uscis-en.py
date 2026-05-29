#!/usr/bin/env python3
"""Injeta popup USCIS inline em todas as páginas /en/."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN = ROOT / "en"
CSS_FILE = ROOT / "pt-br-uscis-popup.css"
JS_FILE = ROOT / "en-uscis-popup.js"
STYLE_MARKER = "<!-- site-uscis-popup-en-style -->"
SCRIPT_MARKER = "<!-- site-uscis-popup-en -->"
SKIP_DIRS = {"wp-content", "wp-includes", "wp-json", "feed", "comments", "author"}

OLD_SCRIPT_RE = re.compile(
	r"\n<!-- site-uscis-popup-en -->.*?(?=\n</body>)",
	re.DOTALL,
)
OLD_STYLE_RE = re.compile(
	r"\n<!-- site-uscis-popup-en-style -->.*?</style>\n",
	re.DOTALL,
)


def build_style_block() -> str:
	css = CSS_FILE.read_text(encoding="utf-8").strip()
	return (
		f"\n{STYLE_MARKER}\n"
		f'<style id="en-uscis-popup-css">\n{css}\n</style>\n'
	)


def build_script_block() -> str:
	js = JS_FILE.read_text(encoding="utf-8").strip()
	return f"\n{SCRIPT_MARKER}\n<script id=\"en-uscis-popup-js\">\n{js}\n</script>\n"


def apply(path: Path, style_block: str, script_block: str) -> bool:
	text = path.read_text(encoding="utf-8")
	new = OLD_STYLE_RE.sub("", text)
	new = OLD_SCRIPT_RE.sub("", new)

	if "</head>" not in new or "</body>" not in new:
		return False

	new = new.replace("</head>", f"{style_block}</head>", 1)
	new = new.replace("</body>", f"{script_block}</body>", 1)

	if new != text:
		path.write_text(new, encoding="utf-8")
		return True
	return False


def iter_en_pages() -> list[Path]:
	paths: list[Path] = []
	home = EN / "index.html"
	if home.is_file():
		paths.append(home)
	for child in sorted(EN.iterdir()):
		if not child.is_dir() or child.name in SKIP_DIRS or child.name.startswith("."):
			continue
		index = child / "index.html"
		if index.is_file():
			paths.append(index)
	return paths


def main() -> None:
	style_block = build_style_block()
	script_block = build_script_block()
	changed = 0
	for path in iter_en_pages():
		if apply(path, style_block, script_block):
			changed += 1
			print(f"  {path.relative_to(ROOT)}")
	print(f"Concluído: {changed} página(s).")


if __name__ == "__main__":
	main()
