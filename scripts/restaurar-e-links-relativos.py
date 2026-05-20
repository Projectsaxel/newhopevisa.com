#!/usr/bin/env python3
"""Restaura HTML do site ao vivo e converte links absolutos para relativos."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
# \s em raw string = whitespace; evita parar na letra "s"
URL_TAIL = r'[^"\'<>\s]*'
PLAIN_URL_RE = re.compile(
	rf"https?://(?:www\.)?newhopevisa\.com(?:/{URL_TAIL})?",
	re.IGNORECASE,
)
ESCAPED_URL_RE = re.compile(
	rf"https?:\\/\\/(?:www\.)?newhopevisa\.com(?:\\/{URL_TAIL})?",
	re.IGNORECASE,
)
ROOT_PATH_RE = re.compile(
	rf'(?<=["\'\s(=])/(?:(?:pt-br|en|es)(?:/{URL_TAIL})?|wp-content/{URL_TAIL}|wp-includes/{URL_TAIL}|wp-json/{URL_TAIL}|wp-admin/{URL_TAIL})',
)
ASSET_SUFFIXES = (
	".html",
	".htm",
	".css",
	".js",
	".json",
	".rss",
	".xml",
	".webp",
	".jpg",
	".jpeg",
	".png",
	".gif",
	".svg",
	".ico",
	".pdf",
	".php",
	".woff",
	".woff2",
	".ttf",
	".eot",
)


def url_to_path(url_tail: str) -> tuple[str, str, str]:
	path, _, fragment = url_tail.partition("#")
	path, _, query = path.partition("?")
	path = unquote(path.strip("/"))
	query = ("?" + query) if query else ""
	fragment = ("#" + fragment) if fragment else ""
	return path, query, fragment


SYSTEM_PREFIXES = (
	"wp-content/",
	"wp-includes/",
	"wp-json/",
	"wp-admin/",
	"feed/",
	"comments/",
	"author/",
	"xmlrpc.php",
)


def target_path(path: str) -> str:
	if not path:
		return "index.html"
	if path.lower().endswith(ASSET_SUFFIXES):
		return path
	if path.startswith(SYSTEM_PREFIXES) or path in {p.rstrip("/") for p in SYSTEM_PREFIXES}:
		return path
	if any(
		marker in path
		for marker in ("/wp-content/", "/wp-includes/", "/wp-json/", "/wp-admin/")
	):
		return path
	return f"{path}/index.html"


def to_relative(file_dir: Path, site_path: str, query: str, fragment: str) -> str:
	rel = os.path.relpath(target_path(site_path), file_dir.as_posix() or ".")
	return rel.replace("\\", "/") + query + fragment


def convert_text(text: str, file_dir: Path) -> str:
	def replace_url(full: str, escaped: bool) -> str:
		tail = full.split("newhopevisa.com", 1)[-1]
		if escaped:
			tail = tail.lstrip("\\/").replace("\\/", "/")
		else:
			tail = tail.lstrip("/")
		path, query, fragment = url_to_path(tail)
		relative = to_relative(file_dir, path, query, fragment)
		return relative.replace("/", "\\/") if escaped else relative

	def plain_replace(match: re.Match[str]) -> str:
		return replace_url(match.group(0), escaped=False)

	def escaped_replace(match: re.Match[str]) -> str:
		return replace_url(match.group(0), escaped=True)

	def root_path_replace(match: re.Match[str]) -> str:
		raw = match.group(0).lstrip("/")
		path, query, fragment = url_to_path(raw)
		return to_relative(file_dir, path, query, fragment)

	text = PLAIN_URL_RE.sub(plain_replace, text)
	text = ESCAPED_URL_RE.sub(escaped_replace, text)
	text = ROOT_PATH_RE.sub(root_path_replace, text)
	return text


def restore_html_files() -> int:
	count = 0
	for html in sorted(ROOT.rglob("index.html")):
		if "scripts" in html.parts:
			continue
		rel = html.relative_to(ROOT).parent
		url = "https://newhopevisa.com/" if rel == Path(".") else f"https://newhopevisa.com/{rel}/"
		result = subprocess.run(
			["curl", "-sL", url, "-o", str(html)],
			capture_output=True,
			text=True,
		)
		if result.returncode != 0:
			print(f"Erro ao baixar {url}: {result.stderr}", file=sys.stderr)
			continue
		count += 1
	return count


def convert_all() -> tuple[int, int]:
	files = 0
	remaining = 0
	extensions = {".html", ".json", ".rss", ".xml"}

	for path in ROOT.rglob("*"):
		if path.suffix.lower() not in extensions or "scripts" in path.parts:
			continue
		original = path.read_text(encoding="utf-8")
		updated = convert_text(original, path.parent.relative_to(ROOT))
		if updated != original:
			path.write_text(updated, encoding="utf-8")
			files += 1
		remaining += len(PLAIN_URL_RE.findall(updated))
		remaining += len(ESCAPED_URL_RE.findall(updated))

	return files, remaining


def fix_oembed_hrefs() -> int:
	count = 0
	oembed_tag = re.compile(
		r'<link rel="alternate" title="oEmbed[^"]*"[^>]*href="[^"]*newhopevisa\.com[^"]*"[^>]*/>\s*',
		re.IGNORECASE,
	)
	for path in ROOT.rglob("*.html"):
		text = path.read_text(encoding="utf-8")
		new_text = oembed_tag.sub("", text)
		if new_text != text:
			path.write_text(new_text, encoding="utf-8")
			count += 1
	return count


def fix_system_index_suffix() -> int:
	count = 0
	replacements = [
		("wp-json/index.html", "wp-json/"),
		("wp-json\\/index.html", "wp-json\\/"),
		("wp-admin/index.html", "wp-admin/"),
		("/assets/index.html", "/assets/"),
		("assets\\/index.html", "assets\\/"),
		("embed/index.html?", "embed?"),
	]
	for path in ROOT.rglob("*"):
		if path.suffix.lower() not in {".html", ".json", ".rss", ".xml"}:
			continue
		if "scripts" in path.parts:
			continue
		text = path.read_text(encoding="utf-8")
		new_text = text
		for old, new in replacements:
			new_text = new_text.replace(old, new)
		if new_text != text:
			path.write_text(new_text, encoding="utf-8")
			count += 1
	return count


def main() -> None:
	convert_only = "--convert-only" in sys.argv

	if not convert_only:
		print("Restaurando HTML do site ao vivo...")
		restored = restore_html_files()
		print(f"Páginas restauradas: {restored}")

	print("Convertendo links absolutos...")
	changed, remaining = convert_all()
	print(f"Arquivos alterados: {changed}")
	print(f"URLs absolutas restantes: {remaining}")

	oembed = fix_oembed_hrefs()
	print(f"oEmbed removidos: {oembed}")

	fixed = fix_system_index_suffix()
	print(f"Paths de sistema corrigidos: {fixed}")


if __name__ == "__main__":
	main()
