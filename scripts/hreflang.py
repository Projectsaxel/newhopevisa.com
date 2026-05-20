#!/usr/bin/env python3
"""Insere link rel=alternate hreflang em todas as páginas do espelho."""

from __future__ import annotations

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKER = '<!-- site-hreflang -->'
HREFLANG_BLOCK_RE = re.compile(
	r"\n<!-- site-hreflang -->.*?</head>",
	re.DOTALL,
)

# slug lógico -> caminho por idioma (sem barra inicial)
PAGES: dict[str, dict[str, str]] = {
	"landing": {
		"pt-br": "pt-br/",
		"en": "en/",
		"es": "es/",
	},
	"home": {
		"pt-br": "pt-br/",
		"en": "en/",
		"es": "es/",
	},
	"servicos": {
		"pt-br": "pt-br/servicos/",
		"en": "en/services/",
		"es": "es/servicios/",
	},
	"taxas": {
		"pt-br": "pt-br/taxas-dos-servicos/",
		"en": "en/fee-schedule/",
		"es": "es/tarifas-de-servicios/",
	},
	"quem-somos": {
		"pt-br": "pt-br/quem-somos/",
		"en": "en/about-us/",
		"es": "es/quienes-somos/",
	},
	"contato": {
		"pt-br": "pt-br/contato/",
		"en": "en/contact-us/",
		"es": "es/contacto/",
	},
	"privacidade": {
		"pt-br": "pt-br/politica-de-privacidade/",
		"en": "en/privacy-policy/",
		"es": "es/politica-de-privacidad/",
	},
	"termos": {
		"pt-br": "pt-br/termos-de-uso/",
		"en": "en/terms-of-use/",
		"es": "es/terminos-de-uso/",
	},
	"cookies": {
		"pt-br": "pt-br/politica-de-cookies/",
		"en": "en/cookie-policy/",
		"es": "es/politica-de-cookies/",
	},
	"visto-trabalho": {
		"pt-br": "pt-br/visto-de-trabalho/",
		"en": "en/work-permit/",
		"es": "es/permiso-de-trabajo/",
	},
	"documentos-viagem": {
		"pt-br": "pt-br/documentos-de-viagem/",
		"en": "en/travel-documents/",
		"es": "es/documentos-de-viaje/",
	},
	"peticao-familiar": {
		"pt-br": "pt-br/peticao-familiar/",
		"en": "en/family-petitions/",
		"es": "es/peticion-familiar/",
	},
	"ajuste-status": {
		"pt-br": "pt-br/ajuste-de-status/",
		"en": "en/adjustment-of-status/",
		"es": "es/ajuste-de-estatus/",
	},
	"processamento-consular": {
		"pt-br": "pt-br/processamento-consular/",
		"en": "en/consular-processing/",
		"es": "es/procesamiento-consular/",
	},
	"naturalizacao": {
		"pt-br": "pt-br/naturalizacao/",
		"en": "en/naturalization/",
		"es": "es/naturalizacion/",
	},
	"renovacao-i90": {
		"pt-br": "pt-br/renovacao-de-residencia-i-90/",
		"en": "en/residence-renewals-i-90/",
		"es": "es/renovacion-de-residencia-i-90/",
	},
	"waivers": {
		"pt-br": "pt-br/waivers/",
		"en": "en/waivers/",
		"es": "es/waivers/",
	},
	"vawa": {
		"pt-br": "pt-br/vawa/",
		"en": "en/vawa/",
		"es": "es/vawa/",
	},
	"tps": {
		"pt-br": "pt-br/status-de-protecao-temporaria-tps/",
		"en": "en/temporary-protected-status-tps/",
		"es": "es/estatus-de-proteccion-temporal-tps/",
	},
}

# slug da pasta -> chave lógica
SLUG_TO_KEY = {
	"": "home",
	"servicos": "servicos",
	"services": "servicos",
	"taxas-dos-servicos": "taxas",
	"fee-schedule": "taxas",
	"quem-somos": "quem-somos",
	"about-us": "quem-somos",
	"contato": "contato",
	"contact-us": "contato",
	"politica-de-privacidade": "privacidade",
	"privacy-policy": "privacidade",
	"termos-de-uso": "termos",
	"terms-of-use": "termos",
	"terminos-de-uso": "termos",
	"politica-de-cookies": "cookies",
	"cookie-policy": "cookies",
	"visto-de-trabalho": "visto-trabalho",
	"work-permit": "visto-trabalho",
	"documentos-de-viagem": "documentos-viagem",
	"travel-documents": "documentos-viagem",
	"peticao-familiar": "peticao-familiar",
	"family-petitions": "peticao-familiar",
	"ajuste-de-status": "ajuste-status",
	"adjustment-of-status": "ajuste-status",
	"processamento-consular": "processamento-consular",
	"consular-processing": "processamento-consular",
	"naturalizacao": "naturalizacao",
	"naturalization": "naturalizacao",
	"renovacao-de-residencia-i-90": "renovacao-i90",
	"residence-renewals-i-90": "renovacao-i90",
	"waivers": "waivers",
	"vawa": "vawa",
	"status-de-protecao-temporaria-tps": "tps",
	"temporary-protected-status-tps": "tps",
	"servicios": "servicos",
	"tarifas-de-servicios": "taxas",
	"quienes-somos": "quem-somos",
	"contacto": "contato",
	"politica-de-privacidad": "privacidade",
	"permiso-de-trabajo": "visto-trabalho",
	"documentos-de-viaje": "documentos-viagem",
	"peticion-familiar": "peticao-familiar",
	"ajuste-de-estatus": "ajuste-status",
	"procesamiento-consular": "processamento-consular",
	"naturalizacion": "naturalizacao",
	"renovacion-de-residencia-i-90": "renovacao-i90",
	"estatus-de-proteccion-temporal-tps": "tps",
}

HREFLANG_CODES = {
	"pt-br": "pt-BR",
	"en": "en",
	"es": "es",
}


def page_key_for_file(path: Path) -> str | None:
	rel = path.relative_to(ROOT)
	if rel == Path("index.html"):
		return "landing"
	parts = rel.parts
	if len(parts) == 2 and parts[1] == "index.html":
		lang = parts[0]
		return "home" if lang in HREFLANG_CODES else None
	if len(parts) != 3 or parts[2] != "index.html":
		return None
	lang, slug = parts[0], parts[1]
	if lang not in HREFLANG_CODES:
		return None
	return SLUG_TO_KEY.get(slug)


def relative_href(from_dir: Path, target_site_path: str) -> str:
	"""Caminho relativo de from_dir até target_site_path (ex: en/services/)."""
	target = target_site_path.rstrip("/")
	from_posix = from_dir.as_posix()
	rel = os.path.relpath(target, from_posix)
	if not rel.endswith("/"):
		rel += "/"
	return rel


def build_hreflang_block(path: Path, page_key: str) -> str:
	alternates = PAGES[page_key]
	from_dir = path.parent
	lines = [MARKER]
	for lang, site_path in alternates.items():
		href = relative_href(from_dir, site_path)
		code = HREFLANG_CODES[lang]
		lines.append(f'<link rel="alternate" hreflang="{code}" href="{href}" />')
	lines.append('<link rel="alternate" hreflang="x-default" href="/" />')
	return "\n".join(lines) + "\n"


def apply_file(path: Path) -> bool:
	page_key = page_key_for_file(path)
	if not page_key:
		return False

	text = path.read_text(encoding="utf-8")
	block = build_hreflang_block(path, page_key)

	if MARKER in text:
		text = HREFLANG_BLOCK_RE.sub(f"\n{block}</head>", text, count=1)
	else:
		if "</head>" not in text:
			return False
		text = text.replace("</head>", f"\n{block}</head>", 1)

	if text == path.read_text(encoding="utf-8"):
		return False
	path.write_text(text, encoding="utf-8")
	return True


def main() -> None:
	changed = 0
	for html in sorted(ROOT.rglob("index.html")):
		if "scripts" in html.parts:
			continue
		if apply_file(html):
			changed += 1
	print(f"Páginas com hreflang atualizado: {changed}")


if __name__ == "__main__":
	main()
