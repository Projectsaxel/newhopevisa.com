#!/usr/bin/env python3
"""Gera robots.txt e sitemaps XML para newhopevisa.com."""

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://newhopevisa.com"

# Importa mapa de páginas do hreflang (mesma fonte de verdade)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from hreflang import HREFLANG_CODES, PAGES  # noqa: E402

SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XHTML_NS = "http://www.w3.org/1999/xhtml"

PRIORITY = {
	"landing": "1.0",
	"home": "0.9",
	"servicos": "0.85",
	"taxas": "0.85",
	"quem-somos": "0.8",
	"contato": "0.8",
	"privacidade": "0.4",
	"termos": "0.4",
	"cookies": "0.4",
}
DEFAULT_PRIORITY = "0.75"

CHANGEFREQ = {
	"landing": "monthly",
	"home": "weekly",
	"privacidade": "yearly",
	"termos": "yearly",
	"cookies": "yearly",
}
DEFAULT_CHANGEFREQ = "monthly"

LASTMOD_RE = re.compile(
	r'<meta property="article:modified_time" content="([^"]+)"'
)


def abs_url(site_path: str) -> str:
	path = site_path if site_path.endswith("/") else f"{site_path}/"
	return f"{DOMAIN}/{path}" if path != "/" else f"{DOMAIN}/"


def html_path_for(site_path: str) -> Path:
	if site_path in ("", "/"):
		return ROOT / "index.html"
	return ROOT / site_path.strip("/") / "index.html"


def lastmod_for(site_path: str) -> str:
	html = html_path_for(site_path)
	if not html.is_file():
		return datetime.now(timezone.utc).strftime("%Y-%m-%d")
	text = html.read_text(encoding="utf-8", errors="ignore")
	match = LASTMOD_RE.search(text)
	if match:
		raw = match.group(1)
		try:
			dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
			return dt.date().isoformat()
		except ValueError:
			pass
	mtime = html.stat().st_mtime
	return datetime.fromtimestamp(mtime, tz=timezone.utc).date().isoformat()


def alternates_for(page_key: str) -> list[tuple[str, str]]:
	langs = PAGES[page_key]
	items: list[tuple[str, str]] = []
	for lang, path in langs.items():
		items.append((HREFLANG_CODES[lang], abs_url(path)))
	items.append(("x-default", f"{DOMAIN}/"))
	return items


def add_url(parent: Element, site_path: str, page_key: str) -> None:
	loc = abs_url(site_path)
	url = SubElement(parent, "url")
	SubElement(url, "loc").text = loc
	SubElement(url, "lastmod").text = lastmod_for(site_path)
	SubElement(url, "changefreq").text = CHANGEFREQ.get(page_key, DEFAULT_CHANGEFREQ)
	SubElement(url, "priority").text = PRIORITY.get(page_key, DEFAULT_PRIORITY)
	for hreflang, href in alternates_for(page_key):
		SubElement(
			url,
			f"{{{XHTML_NS}}}link",
			rel="alternate",
			hreflang=hreflang,
			href=href,
		)


def build_urlset(entries: list[tuple[str, str]]) -> bytes:
	"""entries: [(site_path, page_key), ...]"""
	root = Element("urlset", xmlns=SITEMAP_NS)
	root.set("xmlns:xhtml", XHTML_NS)
	for site_path, page_key in entries:
		add_url(root, site_path, page_key)
	raw = tostring(root, encoding="utf-8", xml_declaration=True)
	return prettify(raw)


def prettify(data: bytes) -> bytes:
	parsed = minidom.parseString(data)
	return parsed.toprettyxml(indent="  ", encoding="utf-8")


def urls_for_lang(lang: str) -> list[tuple[str, str]]:
	result: list[tuple[str, str]] = []
	for page_key, paths in PAGES.items():
		if page_key == "landing":
			continue
		if lang not in paths:
			continue
		result.append((paths[lang], page_key))
	return sorted(result, key=lambda x: x[0])


def write_robots() -> None:
	content = f"""# https://newhopevisa.com/robots.txt
User-agent: *
Allow: /

Disallow: /scripts/
Disallow: /_downloads.html

Sitemap: {DOMAIN}/sitemap-index.xml
"""
	(ROOT / "robots.txt").write_text(content, encoding="utf-8")


def write_sitemap_index(children: list[tuple[str, str]]) -> None:
	root = Element("sitemapindex", xmlns=SITEMAP_NS)
	now = datetime.now(timezone.utc).date().isoformat()
	for filename, _ in children:
		sitemap = SubElement(root, "sitemap")
		SubElement(sitemap, "loc").text = f"{DOMAIN}/{filename}"
		SubElement(sitemap, "lastmod").text = now
	raw = tostring(root, encoding="utf-8", xml_declaration=True)
	(ROOT / "sitemap-index.xml").write_text(
		prettify(raw).decode("utf-8"), encoding="utf-8"
	)


def main() -> None:
	write_robots()

	children: list[tuple[str, str]] = []

	# Landing (seletor de idioma)
	landing_data = build_urlset([("", "landing")])
	(ROOT / "sitemap-landing.xml").write_bytes(landing_data)
	children.append(("sitemap-landing.xml", "landing"))

	for lang, filename in (
		("pt-br", "sitemap-pt-br.xml"),
		("en", "sitemap-en.xml"),
		("es", "sitemap-es.xml"),
	):
		urls = urls_for_lang(lang)
		data = build_urlset(urls)
		(ROOT / filename).write_bytes(data)
		children.append((filename, lang))

	write_sitemap_index(children)

	# Atalho comum: sitemap.xml = índice
	(ROOT / "sitemap.xml").write_text(
		(ROOT / "sitemap-index.xml").read_text(encoding="utf-8"),
		encoding="utf-8",
	)

	total = 1 + sum(len(urls_for_lang(l)) for l in ("pt-br", "en", "es"))
	print(f"robots.txt + sitemap-index.xml + {len(children)} sitemaps ({total} URLs)")


if __name__ == "__main__":
	main()
