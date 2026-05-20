#!/usr/bin/env python3
"""Cria páginas legais (termos, cookies) e atualiza links no rodapé."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEGAL_DIR = Path(__file__).resolve().parent / "i18n" / "legal"

LANGS = {
	"pt-br": {
		"lang": "pt-BR",
		"og_locale": "pt_BR",
		"in_language": "pt-BR",
		"template": "pt-br/politica-de-privacidade/index.html",
		"privacy_slug": "politica-de-privacidade",
		"terms_slug": "termos-de-uso",
		"cookies_slug": "politica-de-cookies",
		"privacy_title": "Política de Privacidade",
		"terms_title": "Termos de Uso",
		"cookies_title": "Política de Cookies",
		"terms_body": "pt_br_terms.html",
		"cookies_body": "pt_br_cookies.html",
		"terms_desc": "Termos de Uso do site New Hope Immigration Services.",
		"cookies_desc": "Política de Cookies do site New Hope Immigration Services.",
	},
	"en": {
		"lang": "en",
		"og_locale": "en_US",
		"in_language": "en",
		"template": "en/privacy-policy/index.html",
		"privacy_slug": "privacy-policy",
		"terms_slug": "terms-of-use",
		"cookies_slug": "cookie-policy",
		"privacy_title": "Privacy Policy",
		"terms_title": "Terms of Use",
		"cookies_title": "Cookie Policy",
		"terms_body": "en_terms.html",
		"cookies_body": "en_cookies.html",
		"terms_desc": "Terms of Use for the New Hope Immigration Services website.",
		"cookies_desc": "Cookie Policy for the New Hope Immigration Services website.",
	},
	"es": {
		"lang": "es",
		"og_locale": "es_ES",
		"in_language": "es",
		"template": "es/politica-de-privacidad/index.html",
		"privacy_slug": "privacy-policy",
		"terms_slug": "terminos-de-uso",
		"cookies_slug": "politica-de-cookies",
		"privacy_title": "Política de Privacidad",
		"terms_title": "Términos de Uso",
		"cookies_title": "Política de Cookies",
		"terms_body": "es_terms.html",
		"cookies_body": "es_cookies.html",
		"terms_desc": "Términos de Uso del sitio New Hope Immigration Services.",
		"cookies_desc": "Política de Cookies del sitio New Hope Immigration Services.",
	},
}

FOOTER_LEGAL_RE = re.compile(
	r'<div class="elementor-element elementor-element-314807e[^>]*>.*?'
	r'<ul class="elementor-icon-list-items elementor-inline-items">.*?</ul>',
	re.DOTALL,
)
DUPLICATE_UL = (
	'<ul class="elementor-icon-list-items elementor-inline-items">\n'
	'\t\t\t\t\t\t\t<ul class="elementor-icon-list-items elementor-inline-items">'
)

SECTION_RE = re.compile(
	r'<section class="(?:privacy-policy|terms-of-use|cookie-policy)">.*?</section>',
	re.DOTALL,
)


def link_prefix(html_path: Path) -> str:
	rel = html_path.relative_to(ROOT)
	if len(rel.parts) == 2:
		return ""
	return "../"


def footer_legal_block(prefix: str, cfg: dict) -> str:
	items = [
		(cfg["terms_slug"], cfg["terms_title"]),
		(cfg["privacy_slug"], cfg["privacy_title"]),
		(cfg["cookies_slug"], cfg["cookies_title"]),
	]
	lis = []
	for slug, label in items:
		lis.append(
			f'''							<li class="elementor-icon-list-item elementor-inline-item">
											<a href="{prefix}{slug}/">
											<span class="elementor-icon-list-text">{label}</span>
											</a>
									</li>'''
		)
	return (
		'							<ul class="elementor-icon-list-items elementor-inline-items">\n'
		+ "\n".join(lis)
		+ "\n						</ul>"
	)


def build_page(cfg: dict, slug: str, title: str, description: str, body_file: str) -> str:
	template = (ROOT / cfg["template"]).read_text(encoding="utf-8")
	body = (LEGAL_DIR / body_file).read_text(encoding="utf-8").strip()

	text = template
	text = text.replace(f'lang="{cfg["lang"]}"', f'lang="{cfg["lang"]}"', 1)
	text = re.sub(r"<title>.*?</title>", f"<title>{title} - New Hope</title>", text, count=1)
	text = re.sub(
		r'<meta name="description" content="[^"]*"/>',
		f'<meta name="description" content="{description}"/>',
		text,
		count=1,
	)
	text = text.replace(f'content="{cfg["og_locale"]}"', f'content="{cfg["og_locale"]}"')
	text = re.sub(
		r'<meta property="og:title" content="[^"]*" />',
		f'<meta property="og:title" content="{title} - New Hope" />',
		text,
		count=1,
	)
	text = re.sub(
		r'<meta property="og:description" content="[^"]*" />',
		f'<meta property="og:description" content="{description}" />',
		text,
		count=1,
	)
	text = re.sub(
		r'<meta name="twitter:title" content="[^"]*" />',
		f'<meta name="twitter:title" content="{title} - New Hope" />',
		text,
		count=1,
	)
	text = re.sub(
		r'<meta name="twitter:description" content="[^"]*" />',
		f'<meta name="twitter:description" content="{description}" />',
		text,
		count=1,
	)
	text = text.replace('"inLanguage":"en"', f'"inLanguage":"{cfg["in_language"]}"')
	text = text.replace('"inLanguage":"pt-BR"', f'"inLanguage":"{cfg["in_language"]}"')
	text = text.replace('"inLanguage":"es"', f'"inLanguage":"{cfg["in_language"]}"')

	# Títulos visíveis (hero + conteúdo)
	old_privacy = cfg["privacy_title"]
	text = text.replace(
		f'<h1 class="elementor-heading-title elementor-size-default">{old_privacy}</h1>',
		f'<h1 class="elementor-heading-title elementor-size-default">{title}</h1>',
	)
	text = text.replace(
		f'<h2 class="elementor-heading-title elementor-size-default">{old_privacy}</h2>',
		f'<h2 class="elementor-heading-title elementor-size-default">{title}</h2>',
	)

	text = SECTION_RE.sub(body, text, count=1)
	return text


def create_legal_pages() -> int:
	created = 0
	for lang, cfg in LANGS.items():
		pages = [
			(cfg["terms_slug"], cfg["terms_title"], cfg["terms_desc"], cfg["terms_body"]),
			(cfg["cookies_slug"], cfg["cookies_title"], cfg["cookies_desc"], cfg["cookies_body"]),
		]
		for slug, title, desc, body_file in pages:
			out_dir = ROOT / lang / slug
			out_dir.mkdir(parents=True, exist_ok=True)
			html = build_page(cfg, slug, title, desc, body_file)
			(out_dir / "index.html").write_text(html, encoding="utf-8")
			created += 1
			print(f"  {lang}/{slug}/index.html")
	return created


def update_footers() -> int:
	changed = 0
	for lang, cfg in LANGS.items():
		for html in (ROOT / lang).rglob("index.html"):
			text = html.read_text(encoding="utf-8")
			if "elementor-element-314807e" not in text:
				continue
			prefix = link_prefix(html)
			new_ul = footer_legal_block(prefix, cfg)

			new_text, n = FOOTER_LEGAL_RE.subn(new_ul, text, count=1)
			new_text = new_text.replace(DUPLICATE_UL, new_ul.split("\n")[0] + "\n")
			if n and new_text != text:
				html.write_text(new_text, encoding="utf-8")
				changed += 1
	return changed


def main() -> None:
	print("Criando páginas legais...")
	n_pages = create_legal_pages()
	print(f"Páginas criadas/atualizadas: {n_pages}")
	print("Atualizando rodapés...")
	n_footers = update_footers()
	print(f"Rodapés atualizados: {n_footers}")


if __name__ == "__main__":
	main()
