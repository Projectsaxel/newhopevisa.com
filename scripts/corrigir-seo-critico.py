#!/usr/bin/env python3
"""Corrige links EN 404, títulos da home, endereço no rodapé e Schema.org."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from hreflang import page_key_for_file  # noqa: E402
from i18n.schema_config import (  # noqa: E402
	DOMAIN,
	EMAIL,
	FOOTER_ADDRESS,
	HOME_SEO,
	LANDING_SEO,
	ORG_NAME,
	PHONE,
	POSTAL,
	REGION,
	STREET,
	LOCALITY,
	COUNTRY,
	LOGO_PATH,
	SERVICE_SCHEMA_NAMES,
)

SCHEMA_MARKER = "<!-- site-schema-local -->"
SCHEMA_MARKER_RE = re.compile(
	r"<!-- site-schema-local -->.*?</script>\s*(?=</head>)",
	re.DOTALL,
)
RANKMATH_SCHEMA_RE = re.compile(
	r'<script type="application/ld\+json" class="rank-math-schema-pro">.*?</script>\n',
	re.DOTALL,
)

EN_SLUG_FIXES = [
	("servicios/", "services/"),
	("quienes-somos/", "about-us/"),
	("contacto/", "contact-us/"),
	("tarifas-de-servicios/", "fee-schedule/"),
]

FOOTER_PHONE_TAIL = (
	'<h5 class="elementor-heading-title elementor-size-default">+ 1 407 275-6163</h5>'
	"\t\t\t\t</div>\n"
)


def fix_en_links() -> int:
	changed = 0
	for path in (ROOT / "en").rglob("*.html"):
		if "wp-json" in path.parts:
			continue
		text = path.read_text(encoding="utf-8")
		new = text
		for old, new_slug in EN_SLUG_FIXES:
			new = new.replace(f'href="{old}"', f'href="{new_slug}"')
			new = new.replace(f"href='{old}'", f"href='{new_slug}'")
			new = new.replace(f"href=\"../{old}\"", f'href="../{new_slug}"')
			new = new.replace(f"href='../{old}'", f"href='../{new_slug}'")
		if new != text:
			path.write_text(new, encoding="utf-8")
			changed += 1
	return changed


def append_htaccess_en_redirects() -> None:
	htaccess = ROOT / ".htaccess"
	block = "\n# Redirecionamentos 301 — slugs EN incorretos (espanhol)\n<IfModule mod_rewrite.c>\n"
	for old, new in EN_SLUG_FIXES:
		old_path = old.rstrip("/")
		new_path = new.rstrip("/")
		block += f"RewriteRule ^en/{old_path}/?$ /en/{new_path}/ [R=301,L]\n"
	block += "</IfModule>\n"
	text = htaccess.read_text(encoding="utf-8")
	if "slugs EN incorretos" in text:
		text = re.sub(
			r"\n# Redirecionamentos 301 — slugs EN incorretos.*?</IfModule>\n",
			"\n",
			text,
			flags=re.DOTALL,
		)
	htaccess.write_text(text.rstrip() + block, encoding="utf-8")


def lang_for_path(path: Path) -> str | None:
	rel = path.relative_to(ROOT)
	if rel == Path("index.html"):
		return "pt-br"
	if len(rel.parts) >= 1 and rel.parts[0] in HOME_SEO:
		return rel.parts[0]
	return None


def depth_prefix(path: Path) -> str:
	rel = path.relative_to(ROOT)
	if rel == Path("index.html"):
		return ""
	parts = rel.parts
	if len(parts) == 2:
		return ""
	if len(parts) == 3:
		return "../"
	depth = len(parts) - 2
	return "../" * depth


def is_home_index(path: Path) -> bool:
	rel = path.relative_to(ROOT)
	return len(rel.parts) == 2 and rel.parts[1] == "index.html" and rel.parts[0] in HOME_SEO


def is_landing_index(path: Path) -> bool:
	return path.relative_to(ROOT) == Path("index.html")


def is_schema_primary_page(path: Path) -> bool:
	return is_landing_index(path) or is_home_index(path)


def site_base_url(path: Path) -> str:
	rel = path.relative_to(ROOT)
	if rel == Path("index.html"):
		return f"{DOMAIN}/"
	if rel.parts and rel.parts[0] in HOME_SEO:
		return f"{DOMAIN}/{rel.parts[0]}/"
	return f"{DOMAIN}/"


def page_canonical_url(path: Path) -> str:
	rel = path.relative_to(ROOT)
	if rel == Path("index.html"):
		return f"{DOMAIN}/"
	if len(rel.parts) >= 2 and rel.parts[-1] == "index.html":
		return f"{DOMAIN}/{'/'.join(rel.parts[:-1])}/"
	return site_base_url(path)


def build_schema(path: Path, lang: str) -> dict:
	base_url = site_base_url(path)
	page_url = page_canonical_url(path)

	page_key = page_key_for_file(path)
	is_primary = page_key in ("home", "landing")

	org_id = f"{DOMAIN}/#organization"
	local_id = f"{page_url}#localbusiness" if is_primary else f"{DOMAIN}/#localbusiness"
	website_id = f"{page_url}#website"

	local_business: dict = {
		"@type": ["LocalBusiness", "ProfessionalService"],
		"@id": local_id,
		"name": ORG_NAME,
		"url": page_url if is_primary else DOMAIN + "/",
		"image": f"{DOMAIN}{LOGO_PATH}",
		"telephone": PHONE,
		"email": EMAIL,
		"priceRange": "$$",
		"address": {
			"@type": "PostalAddress",
			"streetAddress": STREET,
			"addressLocality": LOCALITY,
			"addressRegion": REGION,
			"postalCode": POSTAL,
			"addressCountry": COUNTRY,
		},
		"geo": {
			"@type": "GeoCoordinates",
			"latitude": 28.5383,
			"longitude": -81.3792,
		},
		"openingHoursSpecification": [
			{
				"@type": "OpeningHoursSpecification",
				"dayOfWeek": [
					"Monday",
					"Tuesday",
					"Wednesday",
					"Thursday",
					"Friday",
				],
				"opens": "09:30",
				"closes": "15:00",
			}
		],
		"areaServed": [
			{"@type": "State", "name": "Florida"},
			{"@type": "Country", "name": "United States"},
		],
		"parentOrganization": {"@id": org_id},
	}

	graph: list[dict] = [
		{
			"@type": "Organization",
			"@id": org_id,
			"name": ORG_NAME,
			"url": DOMAIN + "/",
			"logo": f"{DOMAIN}{LOGO_PATH}",
			"email": EMAIL,
			"telephone": PHONE,
			"sameAs": [
				"https://www.instagram.com/newhopeimmigrationservices",
			],
		},
		local_business,
		{
			"@type": "WebSite",
			"@id": website_id,
			"url": base_url,
			"name": ORG_NAME,
			"publisher": {"@id": org_id},
			"inLanguage": {"pt-br": "pt-BR", "en": "en", "es": "es"}[lang],
		},
	]

	if is_primary:
		seo = LANDING_SEO if page_key == "landing" else HOME_SEO[lang]
		graph.insert(
			0,
			{
				"@type": "WebPage",
				"@id": f"{page_url}#webpage",
				"url": page_url,
				"name": seo["title"],
				"description": seo["description"],
				"isPartOf": {"@id": website_id},
				"about": {"@id": local_id},
				"mainEntity": {"@id": local_id},
				"inLanguage": {"pt-br": "pt-BR", "en": "en", "es": "es"}[lang],
			},
		)
	if page_key and page_key in SERVICE_SCHEMA_NAMES:
		svc_name = SERVICE_SCHEMA_NAMES[page_key][lang]
		graph.append(
			{
				"@type": "Service",
				"@id": f"{page_url}#service",
				"name": svc_name,
				"serviceType": svc_name,
				"provider": {"@id": local_id},
				"areaServed": {"@type": "State", "name": "Florida"},
				"url": page_url,
			}
		)

	return {"@context": "https://schema.org", "@graph": graph}


def remove_rankmath_article_on_home(path: Path) -> bool:
	if not is_schema_primary_page(path):
		return False
	text = path.read_text(encoding="utf-8")
	if '"@type":"Article"' not in text and '"@type": "Article"' not in text:
		if 'class="rank-math-schema-pro"' not in text:
			return False
	new_text = RANKMATH_SCHEMA_RE.sub("", text, count=1)
	if new_text == text:
		return False
	path.write_text(new_text, encoding="utf-8")
	return True


def inject_schema(path: Path) -> bool:
	lang = lang_for_path(path)
	if not lang:
		return False
	text = path.read_text(encoding="utf-8")
	block = SCHEMA_MARKER + "\n"
	block += (
		'<script type="application/ld+json" class="site-schema-local">'
		+ json.dumps(build_schema(path, lang), ensure_ascii=False)
		+ "</script>\n"
	)
	if SCHEMA_MARKER in text:
		new_text = SCHEMA_MARKER_RE.sub(block.strip() + "\n", text, count=1)
	else:
		new_text = text.replace("</head>", f"\n{block.rstrip()}\n</head>", 1)
	if new_text != text:
		path.write_text(new_text, encoding="utf-8")
		return True
	return False


def update_home_seo(path: Path, lang: str) -> bool:
	if is_landing_index(path):
		seo = LANDING_SEO
	elif path.parent.name in HOME_SEO:
		seo = HOME_SEO[lang]
	else:
		return False
	text = path.read_text(encoding="utf-8")
	new = text
	new = re.sub(r"<title>.*?</title>", f"<title>{seo['title']}</title>", new, count=1)
	new = re.sub(
		r'<meta name="description" content="[^"]*"/>',
		f'<meta name="description" content="{seo["description"]}"/>',
		new,
		count=1,
	)
	new = re.sub(
		r'<meta property="og:title" content="[^"]*" />',
		f'<meta property="og:title" content="{seo["title"]}" />',
		new,
		count=1,
	)
	new = re.sub(
		r'<meta property="og:description" content="[^"]*" />',
		f'<meta property="og:description" content="{seo["description"]}" />',
		new,
		count=1,
	)
	new = re.sub(
		r'<meta name="twitter:title" content="[^"]*" />',
		f'<meta name="twitter:title" content="{seo["title"]}" />',
		new,
		count=1,
	)
	new = re.sub(
		r'<meta name="twitter:description" content="[^"]*" />',
		f'<meta name="twitter:description" content="{seo["description"]}" />',
		new,
		count=1,
	)
	if new != text:
		path.write_text(new, encoding="utf-8")
		return True
	return False


def inject_footer_address(path: Path, lang: str) -> bool:
	addr = FOOTER_ADDRESS[lang]
	text = path.read_text(encoding="utf-8")
	if "elementor-element-footer-address" in text:
		return False
	needle = FOOTER_PHONE_TAIL
	if needle not in text:
		return False
	insert = (
		needle
		+ f'\t\t\t\t<div class="elementor-element elementor-element-footer-address elementor-widget elementor-widget-heading" data-widget_type="heading.default">\n'
		f'\t\t\t\t\t<p class="elementor-heading-title elementor-size-default">{addr}</p>\t\t\t\t</div>\n'
	)
	new_text = text.replace(needle, insert, 1)
	path.write_text(new_text, encoding="utf-8")
	return True


def main() -> None:
	print("Corrigindo links EN (404)...")
	print(f"  {fix_en_links()} arquivos")
	append_htaccess_en_redirects()
	print("  .htaccess atualizado")

	schema_n = home_n = addr_n = rankmath_n = 0
	targets = [ROOT / "index.html"]
	for lang in ("pt-br", "en", "es"):
		targets.append(ROOT / lang / "index.html")
		for p in (ROOT / lang).rglob("index.html"):
			if "wp-json" not in p.parts:
				targets.append(p)

	for path in sorted(set(targets)):
		lang = lang_for_path(path)
		if not lang:
			continue
		if remove_rankmath_article_on_home(path):
			rankmath_n += 1
		if inject_schema(path):
			schema_n += 1
		if path.name == "index.html" and (
			is_landing_index(path) or path.parent.name in HOME_SEO
		):
			if update_home_seo(path, lang):
				home_n += 1
		if inject_footer_address(path, lang):
			addr_n += 1

	print(f"Rank Math Article removido (home): {rankmath_n} páginas")
	print(f"Schema injetado: {schema_n} páginas")
	print(f"Home SEO: {home_n} páginas")
	print(f"Endereço no rodapé: {addr_n} páginas")


if __name__ == "__main__":
	main()
