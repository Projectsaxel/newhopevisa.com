#!/usr/bin/env python3
"""Gera llms.txt para pt-br, en e es (https://llmstxt.org/)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://newhopevisa.com"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from hreflang import PAGES  # noqa: E402

# page_key -> (section_key, priority: main|services|legal|optional)
PAGE_META: dict[str, tuple[str, str]] = {
	"home": ("main", "main"),
	"servicos": ("main", "main"),
	"taxas": ("main", "main"),
	"quem-somos": ("main", "main"),
	"contato": ("main", "main"),
	"visto-trabalho": ("services", "main"),
	"documentos-viagem": ("services", "main"),
	"peticao-familiar": ("services", "main"),
	"ajuste-status": ("services", "main"),
	"processamento-consular": ("services", "main"),
	"naturalizacao": ("services", "main"),
	"renovacao-i90": ("services", "main"),
	"waivers": ("services", "main"),
	"vawa": ("services", "main"),
	"tps": ("services", "main"),
	"privacidade": ("legal", "main"),
	"termos": ("legal", "main"),
	"cookies": ("legal", "main"),
}

LOCALE: dict[str, dict[str, str | dict[str, str]]] = {
	"pt-br": {
		"lang_label": "Português (Brasil)",
		"summary": (
			"New Hope Immigration Services é uma organização sem fins lucrativos na "
			"Flórida (EUA) que oferece preparação de documentos e orientação em processos "
			"de imigração a baixo custo. Não somos escritório de advocacia. Telefone: "
			"+1 407 275-6163. Site em português brasileiro."
		),
		"sections": {
			"main": "Páginas principais",
			"services": "Serviços de imigração",
			"legal": "Políticas e termos legais",
			"optional": "Opcional",
			"languages": "Outros idiomas",
			"meta": "Metadados",
		},
		"pages": {
			"home": ("Início", "Página inicial do site em português."),
			"servicos": ("Serviços", "Visão geral dos serviços de imigração oferecidos."),
			"taxas": ("Taxas dos serviços", "Tabela de taxas de serviço (não inclui taxas USCIS)."),
			"quem-somos": ("Quem somos", "Missão, equipe e história da organização."),
			"contato": ("Contato", "Formulário e dados para falar com a equipe."),
			"visto-trabalho": ("Visto de trabalho (EAD)", "Autorização de emprego e permisos de trabalho."),
			"documentos-viagem": ("Documentos de viagem", "Advance parole e documentação de viagem."),
			"peticao-familiar": ("Petição familiar", "Reunificação familiar e petições I-130."),
			"ajuste-status": ("Ajuste de status", "Green card dentro dos EUA (I-485)."),
			"processamento-consular": ("Processamento consular", "Vistos de imigrante via consulado."),
			"naturalizacao": ("Naturalização", "Cidadania americana (Form N-400)."),
			"renovacao-i90": ("Renovação de residência (I-90)", "Renovação ou substituição de green card."),
			"waivers": ("Waivers", "Perdões de inadmissibilidade."),
			"vawa": ("VAWA", "Violência doméstica — petição VAWA."),
			"tps": ("TPS", "Temporary Protected Status."),
			"privacidade": ("Política de privacidade", "Coleta e uso de dados pessoais."),
			"termos": ("Termos de uso", "Regras de uso do site e dos serviços."),
			"cookies": ("Política de cookies", "Uso de cookies e tecnologias de rastreamento."),
		},
		"other_llms": {
			"en": ("English", "Versão em inglês do site."),
			"es": ("Español", "Versão em espanhol do site."),
		},
	},
	"en": {
		"lang_label": "English",
		"summary": (
			"New Hope Immigration Services is a nonprofit organization in Florida (USA) "
			"providing low-cost immigration document preparation and guidance. We are not "
			"a law firm. Phone: +1 407 275-6163. English-language site."
		),
		"sections": {
			"main": "Main pages",
			"services": "Immigration services",
			"legal": "Legal policies and terms",
			"optional": "Optional",
			"languages": "Other languages",
			"meta": "Metadata",
		},
		"pages": {
			"home": ("Home", "English homepage."),
			"servicos": ("Services", "Overview of immigration services offered."),
			"taxas": ("Fee schedule", "Service fees (USCIS filing fees not included)."),
			"quem-somos": ("About us", "Mission, team, and organization background."),
			"contato": ("Contact us", "Contact form and ways to reach the team."),
			"visto-trabalho": ("Work permit (EAD)", "Employment authorization documents."),
			"documentos-viagem": ("Travel documents", "Advance parole and travel authorization."),
			"peticao-familiar": ("Family petitions", "Family reunification and I-130 petitions."),
			"ajuste-status": ("Adjustment of status", "Green card while in the U.S. (I-485)."),
			"processamento-consular": ("Consular processing", "Immigrant visas through U.S. consulates."),
			"naturalizacao": ("Naturalization", "U.S. citizenship (Form N-400)."),
			"renovacao-i90": ("Residence renewal (I-90)", "Green card renewal or replacement."),
			"waivers": ("Waivers", "Inadmissibility waivers."),
			"vawa": ("VAWA", "Domestic violence — VAWA self-petition."),
			"tps": ("TPS", "Temporary Protected Status."),
			"privacidade": ("Privacy policy", "How personal data is collected and used."),
			"termos": ("Terms of use", "Website and service usage rules."),
			"cookies": ("Cookie policy", "Cookies and tracking technologies."),
		},
		"other_llms": {
			"pt-br": ("Português (Brasil)", "Brazilian Portuguese version of the site."),
			"es": ("Español", "Spanish version of the site."),
		},
	},
	"es": {
		"lang_label": "Español",
		"summary": (
			"New Hope Immigration Services es una organización sin fines de lucro en "
			"Florida (EE. UU.) que ofrece preparación de documentos y orientación en "
			"procesos de inmigración a bajo costo. No somos un bufete de abogados. "
			"Teléfono: +1 407 275-6163. Sitio en español."
		),
		"sections": {
			"main": "Páginas principales",
			"services": "Servicios de inmigración",
			"legal": "Políticas y términos legales",
			"optional": "Opcional",
			"languages": "Otros idiomas",
			"meta": "Metadatos",
		},
		"pages": {
			"home": ("Inicio", "Página principal del sitio en español."),
			"servicos": ("Servicios", "Resumen de los servicios de inmigración."),
			"taxas": ("Tarifas", "Tabla de tarifas de servicio (no incluye tasas del USCIS)."),
			"quem-somos": ("Quiénes somos", "Misión, equipo e historia de la organización."),
			"contato": ("Contacto", "Formulario y datos de contacto."),
			"visto-trabalho": ("Permiso de trabajo (EAD)", "Autorización de empleo."),
			"documentos-viagem": ("Documentos de viaje", "Advance parole y autorización de viaje."),
			"peticao-familiar": ("Peticiones familiares", "Reunificación familiar e I-130."),
			"ajuste-status": ("Ajuste de estatus", "Green card dentro de EE. UU. (I-485)."),
			"processamento-consular": ("Procesamiento consular", "Visas de inmigrante en consulado."),
			"naturalizacao": ("Naturalización", "Ciudadanía estadounidense (Form N-400)."),
			"renovacao-i90": ("Renovación de residencia (I-90)", "Renovación o reemplazo de green card."),
			"waivers": ("Waivers", "Perdones de inadmisibilidad."),
			"vawa": ("VAWA", "Violencia doméstica — petición VAWA."),
			"tps": ("TPS", "Temporary Protected Status."),
			"privacidade": ("Política de privacidad", "Recopilación y uso de datos personales."),
			"termos": ("Términos de uso", "Reglas de uso del sitio y los servicios."),
			"cookies": ("Política de cookies", "Cookies y tecnologías de seguimiento."),
		},
		"other_llms": {
			"pt-br": ("Português (Brasil)", "Versión del sitio en portugués brasileño."),
			"en": ("English", "Versión del sitio en inglés."),
		},
	},
}


def abs_url(site_path: str) -> str:
	path = site_path if site_path.endswith("/") else f"{site_path}/"
	return f"{DOMAIN}/{path}"


def build_llms_txt(lang: str) -> str:
	cfg = LOCALE[lang]
	sections: dict[str, list[str]] = {
		"main": [],
		"services": [],
		"legal": [],
		"optional": [],
	}

	for page_key, paths in PAGES.items():
		if page_key == "landing":
			continue
		if lang not in paths:
			continue
		meta = PAGE_META.get(page_key, ("main", "main"))
		section_id = meta[0]
		priority = meta[1]
		if priority == "optional":
			section_id = "optional"

		page_cfg = cfg["pages"][page_key]  # type: ignore[index]
		title, desc = page_cfg  # type: ignore[misc]
		url = abs_url(paths[lang])
		line = f"- [{title}]({url}): {desc}"
		sections.setdefault(section_id, []).append(line)

	lines: list[str] = [
		f"# New Hope Immigration Services ({cfg['lang_label']})",
		"",
		f"> {cfg['summary']}",
		"",
	]

	sec_titles = cfg["sections"]  # type: ignore[assignment]
	for sec_id in ("main", "services", "legal"):
		if sections.get(sec_id):
			lines.append(f"## {sec_titles[sec_id]}")
			lines.append("")
			lines.extend(sections[sec_id])
			lines.append("")

	lines.append(f"## {sec_titles['languages']}")
	lines.append("")
	for other_lang, (label, desc) in cfg["other_llms"].items():  # type: ignore[union-attr]
		lines.append(f"- [{label}]({DOMAIN}/{other_lang}/llms.txt): {desc}")
	lines.append(f"- [Seletor de idioma / Language hub]({DOMAIN}/): Choose PT, EN, or ES.")
	lines.append("")

	lines.append(f"## {sec_titles['meta']}")
	lines.append("")
	lines.append(f"- Canonical base URL: {abs_url(PAGES['home'][lang])}")
	lines.append(f"- Sitemap: {DOMAIN}/sitemap-index.xml")
	lines.append(f"- robots.txt: {DOMAIN}/robots.txt")
	lines.append(f"- llms.txt (this file): {DOMAIN}/{lang}/llms.txt")
	lines.append("")

	return "\n".join(lines).rstrip() + "\n"


def main() -> None:
	for lang in ("pt-br", "en", "es"):
		out = ROOT / lang / "llms.txt"
		out.write_text(build_llms_txt(lang), encoding="utf-8")
		print(f"  {out.relative_to(ROOT)}")
	print("Concluído: 3 arquivos llms.txt")


if __name__ == "__main__":
	main()
