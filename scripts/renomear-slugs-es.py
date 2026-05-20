#!/usr/bin/env python3
"""Renomeia pastas/URLs em /es/ para slugs em espanhol e atualiza referências."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ES = ROOT / "es"

# slug inglês (pasta) -> slug espanhol
SLUG_RENAME: dict[str, str] = {
	"services": "servicios",
	"fee-schedule": "tarifas-de-servicios",
	"about-us": "quienes-somos",
	"contact-us": "contacto",
	"privacy-policy": "politica-de-privacidad",
	"work-permit": "permiso-de-trabajo",
	"travel-documents": "documentos-de-viaje",
	"family-petitions": "peticion-familiar",
	"adjustment-of-status": "ajuste-de-estatus",
	"consular-processing": "procesamiento-consular",
	"naturalization": "naturalizacion",
	"residence-renewals-i-90": "renovacion-de-residencia-i-90",
	"temporary-protected-status-tps": "estatus-de-proteccion-temporal-tps",
}

# hreflang.py paths (es) — aplicado após renomear pastas
HREFLANG_ES_PATHS = {
	"servicos": "es/servicios/",
	"taxas": "es/tarifas-de-servicios/",
	"quem-somos": "es/quienes-somos/",
	"contato": "es/contacto/",
	"privacidade": "es/politica-de-privacidad/",
	"visto-trabalho": "es/permiso-de-trabajo/",
	"documentos-viagem": "es/documentos-de-viaje/",
	"peticao-familiar": "es/peticion-familiar/",
	"ajuste-status": "es/ajuste-de-estatus/",
	"processamento-consular": "es/procesamiento-consular/",
	"naturalizacao": "es/naturalizacion/",
	"renovacao-i90": "es/renovacion-de-residencia-i-90/",
	"tps": "es/estatus-de-proteccion-temporal-tps/",
}

SLUG_TO_KEY_ADD = {
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

TEXT_GLOBS = (".html", ".xml", ".txt", ".py", ".md")

# Ordem: slugs mais longos primeiro (evita substituição parcial)
RENAME_ORDER = sorted(SLUG_RENAME.items(), key=lambda x: -len(x[0]))


def rename_directories() -> int:
	moved = 0
	for old, new in RENAME_ORDER:
		src = ES / old
		dst = ES / new
		if not src.is_dir():
			if dst.is_dir():
				continue
			print(f"  aviso: pasta ausente {src}")
			continue
		if dst.exists():
			raise SystemExit(f"Destino já existe: {dst}")
		shutil.move(str(src), str(dst))
		print(f"  {old}/ -> {new}/")
		moved += 1
	return moved


def replace_in_text(text: str) -> str:
	for old, new in RENAME_ORDER:
		# caminhos absolutos no site
		text = text.replace(f"es/{old}/", f"es/{new}/")
		# hreflang e links entre idiomas
		text = text.replace(f"/es/{old}/", f"/es/{new}/")
		# dentro de /es/ (relativos)
		text = text.replace(f"../{old}/", f"../{new}/")
		text = text.replace(f'href="{old}/"', f'href="{new}/"')
		text = text.replace(f"href='{old}/'", f"href='{new}/'")
	return text


def update_files() -> int:
	changed = 0
	for path in ROOT.rglob("*"):
		if not path.is_file():
			continue
		if ".git" in path.parts or path.suffix not in TEXT_GLOBS:
			continue
		if path.name == "renomear-slugs-es.py":
			continue
		text = path.read_text(encoding="utf-8", errors="ignore")
		new_text = replace_in_text(text)
		if new_text != text:
			path.write_text(new_text, encoding="utf-8")
			changed += 1
	return changed


def patch_hreflang_py() -> None:
	path = ROOT / "scripts" / "hreflang.py"
	text = path.read_text(encoding="utf-8")
	for page_key, es_path in HREFLANG_ES_PATHS.items():
		# "es": "es/services/",
		pattern = rf'("{page_key}": \{{[^}}]*"es": )"es/[^"]+"'
		match = re.search(pattern, text, re.DOTALL)
		if not match:
			continue
		old_es = re.search(rf'"{page_key}": \{{.*?"es": "(es/[^"]+)"', text, re.DOTALL)
		if old_es:
			text = text.replace(old_es.group(1), es_path.rstrip("/") + "/", 1)

	# Atualização direta por chave conhecida
	replacements = {
		'"es": "es/services/"': '"es": "es/servicios/"',
		'"es": "es/fee-schedule/"': '"es": "es/tarifas-de-servicios/"',
		'"es": "es/about-us/"': '"es": "es/quienes-somos/"',
		'"es": "es/contact-us/"': '"es": "es/contacto/"',
		'"es": "es/privacy-policy/"': '"es": "es/politica-de-privacidad/"',
		'"es": "es/work-permit/"': '"es": "es/permiso-de-trabajo/"',
		'"es": "es/travel-documents/"': '"es": "es/documentos-de-viaje/"',
		'"es": "es/family-petitions/"': '"es": "es/peticion-familiar/"',
		'"es": "es/adjustment-of-status/"': '"es": "es/ajuste-de-estatus/"',
		'"es": "es/consular-processing/"': '"es": "es/procesamiento-consular/"',
		'"es": "es/naturalization/"': '"es": "es/naturalizacion/"',
		'"es": "es/residence-renewals-i-90/"': '"es": "es/renovacion-de-residencia-i-90/"',
		'"es": "es/temporary-protected-status-tps/"': '"es": "es/estatus-de-proteccion-temporal-tps/"',
	}
	for old, new in replacements.items():
		text = text.replace(old, new)

	# SLUG_TO_KEY: inserir entradas ES após temporary-protected-status-tps
	marker = '\t"temporary-protected-status-tps": "tps",\n}'
	if marker in text:
		extra = '\t"temporary-protected-status-tps": "tps",\n'
		for slug, key in SLUG_TO_KEY_ADD.items():
			extra += f'\t"{slug}": "{key}",\n'
		text = text.replace(marker, extra + "}")

	path.write_text(text, encoding="utf-8")


def append_htaccess_redirects() -> None:
	htaccess = ROOT / ".htaccess"
	block = "\n# Redirecionamentos 301 — slugs ES antigos (inglês) -> espanhol\n"
	block += "<IfModule mod_rewrite.c>\n"
	for old, new in sorted(SLUG_RENAME.items()):
		block += f"RewriteRule ^es/{old}/?$ /es/{new}/ [R=301,L]\n"
	block += "</IfModule>\n"
	text = htaccess.read_text(encoding="utf-8")
	if "slugs ES antigos" in text:
		# remove bloco anterior
		text = re.sub(
			r"\n# Redirecionamentos 301 — slugs ES antigos.*?</IfModule>\n",
			"\n",
			text,
			flags=re.DOTALL,
		)
	htaccess.write_text(text.rstrip() + block, encoding="utf-8")


def main() -> None:
	print("Renomeando pastas em es/…")
	n_dirs = rename_directories()
	print(f"Pastas movidas: {n_dirs}")
	print("Atualizando referências nos arquivos…")
	n_files = update_files()
	print(f"Arquivos alterados: {n_files}")
	print("Atualizando scripts/hreflang.py…")
	patch_hreflang_py()
	print("Adicionando redirects 301 em .htaccess…")
	append_htaccess_redirects()
	print("Concluído. Rode: python3 scripts/hreflang.py && python3 scripts/gerar-llms-txt.py && python3 scripts/gerar-sitemap.py")


if __name__ == "__main__":
	main()
