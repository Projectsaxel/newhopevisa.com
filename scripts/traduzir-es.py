#!/usr/bin/env python3
"""Traduz páginas /es/ e corrige metas; injeta corpos em espanhol."""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = Path(__file__).resolve().parent / "i18n"
BODIES = I18N / "bodies"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n.es_meta import ES_PAGE_META  # noqa: E402
from i18n.es_strings import ES_REPLACEMENTS  # noqa: E402

TEXT_EDITOR_RE = re.compile(
	r'(<div class="elementor-element elementor-element-ebc7ca2 elementor-widget elementor-widget-text-editor"[^>]*>\s*)(.*?)(\s*</div>)',
	re.DOTALL,
)
PRIVACY_SECTION_RE = re.compile(
	r"(<section class=\"privacy-policy\">)(.*?)(</section>)",
	re.DOTALL,
)

BODY_SLUGS = {
	"work-permit",
	"waivers",
	"vawa",
	"travel-documents",
	"temporary-protected-status-tps",
	"residence-renewals-i-90",
	"naturalization",
	"family-petitions",
	"consular-processing",
	"adjustment-of-status",
}


def slug_for(path: Path) -> str:
	parts = path.relative_to(ROOT / "es").parts
	return "" if parts == ("index.html",) else parts[0]


def apply_replacements(text: str) -> str:
	for old, new in sorted(ES_REPLACEMENTS.items(), key=lambda x: -len(x[0])):
		text = text.replace(old, new)
	return text


def apply_meta(text: str, title: str, description: str) -> str:
	text = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", text, count=1)
	text = re.sub(
		r'<meta name="description" content="[^"]*"',
		f'<meta name="description" content="{description}"',
		text,
		count=1,
	)
	text = re.sub(
		r'<meta property="og:title" content="[^"]*"',
		f'<meta property="og:title" content="{title}"',
		text,
		count=1,
	)
	text = re.sub(
		r'<meta property="og:description" content="[^"]*"',
		f'<meta property="og:description" content="{description}"',
		text,
		count=1,
	)
	text = re.sub(
		r'<meta name="twitter:title" content="[^"]*"',
		f'<meta name="twitter:title" content="{title}"',
		text,
		count=1,
	)
	text = re.sub(
		r'<meta name="twitter:description" content="[^"]*"',
		f'<meta name="twitter:description" content="{description}"',
		text,
		count=1,
	)
	esc = description.replace("\\", "\\\\").replace('"', '\\"')
	text = re.sub(r'"headline":"[^"]*"', f'"headline":"{title}"', text)
	text = re.sub(r'"name":"[^"]* - New Hope"', f'"name":"{title}"', text)
	text = re.sub(r'"name":"Privacy Policy"', f'"name":"{title}"', text)
	text = re.sub(r'"name":"Home - New Hope"', f'"name":"{title}"', text)
	text = re.sub(
		r'"description":"[^"]*"(?=,"name")',
		f'"description":"{esc}"',
		text,
		count=1,
	)
	return text


def inject_body(text: str, body_file: Path, pattern: re.Pattern[str]) -> str:
	body = body_file.read_text(encoding="utf-8").strip()

	def repl(match: re.Match[str]) -> str:
		return f"{match.group(1)}{body}{match.group(3)}"

	new_text, n = pattern.subn(repl, text, count=1)
	return new_text if n else text


def process_es_page(path: Path) -> bool:
	slug = slug_for(path)
	text = path.read_text(encoding="utf-8")
	orig = text

	text = apply_replacements(text)

	if slug in BODY_SLUGS:
		body_path = BODIES / f"{slug}.html"
		if body_path.is_file():
			text = inject_body(text, body_path, TEXT_EDITOR_RE)

	if slug == "privacy-policy":
		body_path = BODIES / "privacy-policy.html"
		if body_path.is_file():
			body = body_path.read_text(encoding="utf-8").strip()
			# arquivo já inclui <section>
			text, _ = PRIVACY_SECTION_RE.subn(
				lambda m: body if body.startswith("<section") else f"{m.group(1)}{body}{m.group(3)}",
				text,
				count=1,
			)
			text = text.replace(
				"<h2 class=\"elementor-heading-title elementor-size-default\">Privacy Policy</h2>",
				"<h2 class=\"elementor-heading-title elementor-size-default\">Política de Privacidad</h2>",
			)
			text = text.replace(
				"<h1 class=\"elementor-heading-title elementor-size-default\">Privacy Policy</h1>",
				"<h1 class=\"elementor-heading-title elementor-size-default\">Política de Privacidad</h1>",
			)

	if slug in ES_PAGE_META:
		title, desc = ES_PAGE_META[slug]
		text = apply_meta(text, title, desc)

	if text != orig:
		path.write_text(text, encoding="utf-8")
		return True
	return False


def ensure_privacy_page() -> None:
	dst = ROOT / "es" / "privacy-policy" / "index.html"
	if dst.is_file():
		return
	src = ROOT / "en" / "privacy-policy" / "index.html"
	if not src.is_file():
		print("Aviso: en/privacy-policy/index.html não encontrado.", file=sys.stderr)
		return
	dst.parent.mkdir(parents=True, exist_ok=True)
	shutil.copy2(src, dst)
	print("Criado es/politica-de-privacidad/index.html a partir de en/")


def main() -> None:
	ensure_privacy_page()
	changed = 0
	for html in sorted((ROOT / "es").rglob("index.html")):
		if process_es_page(html):
			changed += 1
	print(f"Páginas ES atualizadas: {changed}")


if __name__ == "__main__":
	main()
