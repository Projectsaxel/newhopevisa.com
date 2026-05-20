#!/usr/bin/env python3
"""Preenche atributo alt das imagens e og:image:alt por idioma."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n.img_alt import ALT_BY_FILE, OG_ALT_BY_SLUG  # noqa: E402

IMG_TAG_RE = re.compile(r"<img\b[^>]*>", re.I)
ALT_ATTR_RE = re.compile(r'\balt=(["\'])(.*?)\1', re.I)
OG_ALT_RE = re.compile(
	r'(<meta property="og:image:alt" content=")([^"]*)(" */>)',
	re.I,
)


def lang_for_path(path: Path) -> str | None:
	rel = path.relative_to(ROOT)
	if rel == Path("index.html"):
		return "pt-br"  # landing usa PT como padrão
	parts = rel.parts
	if parts[0] in ("pt-br", "en", "es"):
		return parts[0]
	return None


def slug_for_path(path: Path) -> str | None:
	rel = path.relative_to(ROOT)
	if len(rel.parts) == 3 and rel.parts[2] == "index.html":
		return rel.parts[1]
	return None


def basename_from_tag(tag: str) -> str | None:
	m = re.search(r'\bsrc=(["\'])([^"\']+)\1', tag, re.I)
	if not m:
		return None
	return m.group(2).split("/")[-1].split("?")[0]


def apply_alt_to_tag(tag: str, alt_text: str) -> str:
	escaped = html.escape(alt_text, quote=True)
	if ALT_ATTR_RE.search(tag):
		return ALT_ATTR_RE.sub(f'alt="{escaped}"', tag, count=1)
	return tag.replace("<img", f'<img alt="{escaped}"', 1)


def process_html(path: Path) -> tuple[int, int]:
	lang = lang_for_path(path)
	if not lang:
		return 0, 0

	alts = {fn: texts[lang] for fn, texts in ALT_BY_FILE.items()}
	text = path.read_text(encoding="utf-8")
	img_count = 0

	def repl_img(match: re.Match[str]) -> str:
		nonlocal img_count
		tag = match.group(0)
		base = basename_from_tag(tag)
		if not base or base not in alts:
			return tag
		img_count += 1
		return apply_alt_to_tag(tag, alts[base])

	text = IMG_TAG_RE.sub(repl_img, text)

	og_count = 0
	slug = slug_for_path(path)
	if slug and slug in OG_ALT_BY_SLUG:
		og_alt = OG_ALT_BY_SLUG[slug][lang]
		new_text, n = OG_ALT_RE.subn(
			lambda m: f'{m.group(1)}{html.escape(og_alt, quote=True)}{m.group(3)}',
			text,
			count=1,
		)
		if n:
			text = new_text
			og_count = 1

	if img_count or og_count:
		path.write_text(text, encoding="utf-8")
	return img_count, og_count


def main() -> None:
	total_img = total_og = files = 0
	targets = [ROOT / "index.html"]
	for lang in ("pt-br", "en", "es"):
		targets.extend(
			p
			for p in (ROOT / lang).rglob("index.html")
			if "wp-json" not in p.parts
		)

	for path in sorted(targets):
		n_img, n_og = process_html(path)
		if n_img or n_og:
			files += 1
			total_img += n_img
			total_og += n_og

	print(f"Arquivos atualizados: {files}")
	print(f"Tags <img> com alt: {total_img}")
	print(f"og:image:alt atualizados: {total_og}")


if __name__ == "__main__":
	main()
