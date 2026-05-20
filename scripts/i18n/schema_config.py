"""Dados compartilhados para Schema.org e SEO local."""

from __future__ import annotations

DOMAIN = "https://newhopevisa.com"
ORG_NAME = "New Hope Immigration Services"
PHONE = "+1-407-275-6163"
EMAIL = "email@newhopevisa.com"
STREET = "4300 Lake Margaret Dr"
LOCALITY = "Orlando"
REGION = "FL"
POSTAL = "32812"
COUNTRY = "US"
LOGO_PATH = "/wp-content/uploads/2025/11/new-hope-logo.webp"

LANDING_SEO = {
	"title": "New Hope Immigration Services | Orlando, FL | USA",
	"description": (
		"Nonprofit immigration document preparation in Orlando, FL. "
		"Choose your language: Portuguese, English, or Spanish. Call +1 407 275-6163."
	),
}

HOME_SEO = {
	"pt-br": {
		"title": "Serviços de Imigração nos EUA | Ajuda com Visto | New Hope",
		"description": (
			"New Hope Immigration Services em Orlando, FL: preparação de documentos, "
			"visto de trabalho, green card, naturalização e petição familiar. Ligue +1 407 275-6163."
		),
	},
	"en": {
		"title": "Immigration Services for USA | Visa Help | New Hope",
		"description": (
			"New Hope Immigration Services in Orlando, FL: document preparation, work permits, "
			"green cards, naturalization, and family petitions. Call +1 407 275-6163."
		),
	},
	"es": {
		"title": "Servicios de Inmigración en EE. UU. | Ayuda con Visa | New Hope",
		"description": (
			"New Hope Immigration Services en Orlando, FL: preparación de documentos, permiso de trabajo, "
			"green card, naturalización y peticiones familiares. Llame al +1 407 275-6163."
		),
	},
}

FOOTER_ADDRESS = {
	"pt-br": "4300 Lake Margaret Dr, Orlando, FL 32812",
	"en": "4300 Lake Margaret Dr, Orlando, FL 32812",
	"es": "4300 Lake Margaret Dr, Orlando, FL 32812",
}

SERVICE_SCHEMA_NAMES = {
	"visto-trabalho": {
		"pt-br": "Visto de trabalho e autorização de emprego (EAD)",
		"en": "Work permit and employment authorization (EAD)",
		"es": "Permiso de trabajo y autorización de empleo (EAD)",
	},
	"documentos-viagem": {
		"pt-br": "Documentos de viagem para imigração",
		"en": "Immigration travel documents",
		"es": "Documentos de viaje para inmigración",
	},
	"peticao-familiar": {
		"pt-br": "Petição familiar de imigração",
		"en": "Family immigration petition",
		"es": "Petición familiar de inmigración",
	},
	"ajuste-status": {
		"pt-br": "Ajuste de status para green card",
		"en": "Adjustment of status to green card",
		"es": "Ajuste de estatus a green card",
	},
	"processamento-consular": {
		"pt-br": "Processamento consular de visto",
		"en": "Consular processing for immigrant visa",
		"es": "Procesamiento consular de visa de inmigrante",
	},
	"naturalizacao": {
		"pt-br": "Naturalização e cidadania americana",
		"en": "Naturalization and U.S. citizenship",
		"es": "Naturalización y ciudadanía estadounidense",
	},
	"renovacao-i90": {
		"pt-br": "Renovação de green card (Formulário I-90)",
		"en": "Green card renewal (Form I-90)",
		"es": "Renovación de green card (Formulario I-90)",
	},
	"waivers": {
		"pt-br": "Waiver de inadmissibilidade",
		"en": "Immigration inadmissibility waiver",
		"es": "Waiver de inadmisibilidad",
	},
	"vawa": {
		"pt-br": "Petição VAWA",
		"en": "VAWA self-petition",
		"es": "Petición VAWA",
	},
	"tps": {
		"pt-br": "Status de Proteção Temporária (TPS)",
		"en": "Temporary Protected Status (TPS)",
		"es": "Estatus de Protección Temporal (TPS)",
	},
}
