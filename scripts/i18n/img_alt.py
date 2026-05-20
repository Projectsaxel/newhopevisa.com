"""Textos alt por arquivo de imagem e idioma."""

from __future__ import annotations

# nome do arquivo (basename) -> alt por idioma
ALT_BY_FILE: dict[str, dict[str, str]] = {
	"new-hope-logo.webp": {
		"pt-br": "Logotipo da New Hope Immigration Services",
		"en": "New Hope Immigration Services logo",
		"es": "Logotipo de New Hope Immigration Services",
	},
	"new-hope-logo-invertido.webp": {
		"pt-br": "Logotipo da New Hope Immigration Services em versão clara",
		"en": "New Hope Immigration Services logo, light version",
		"es": "Logotipo de New Hope Immigration Services en versión clara",
	},
	"icon-white-05.png": {
		"pt-br": "Ícone de entrega de passaporte para processo de imigração",
		"en": "Icon for passport submission for immigration process",
		"es": "Icono de entrega de pasaporte para proceso de inmigración",
	},
	"icon-white-04.png": {
		"pt-br": "Ícone de documento de viagem para imigração",
		"en": "Icon for immigration travel document",
		"es": "Icono de documento de viaje para inmigración",
	},
	"icon-white-03.png": {
		"pt-br": "Ícone de agendamento de consulta de imigração",
		"en": "Icon for scheduling an immigration consultation",
		"es": "Icono de agendar consulta de inmigración",
	},
	"woman-getting-visa-documents-in-office.jpg": {
		"pt-br": "Mulher recebendo documentos de visto em escritório de imigração",
		"en": "Woman receiving visa documents at an immigration office",
		"es": "Mujer recibiendo documentos de visa en oficina de inmigración",
	},
	"sq-06.jpg": {
		"pt-br": "Profissional auxiliando cliente com documentação de imigração",
		"en": "Professional helping a client with immigration paperwork",
		"es": "Profesional ayudando a un cliente con documentación de inmigración",
	},
	"thinking-of-america-1024x682.jpg": {
		"pt-br": "Pessoa refletindo sobre o sonho de viver nos Estados Unidos",
		"en": "Person reflecting on the dream of living in the United States",
		"es": "Persona reflexionando sobre el sueño de vivir en Estados Unidos",
	},
	"thinking-of-america.jpg": {
		"pt-br": "Pessoa refletindo sobre o sonho de viver nos Estados Unidos",
		"en": "Person reflecting on the dream of living in the United States",
		"es": "Persona reflexionando sobre el sueño de vivir en Estados Unidos",
	},
	"young-smiling-student-standing-at-a-window-preparing-for-lecture-682x1024.jpg": {
		"pt-br": "Jovem estudante sorrindo à janela, preparando-se para aula",
		"en": "Young smiling student by a window, preparing for class",
		"es": "Joven estudiante sonriente junto a una ventana, preparándose para clase",
	},
	"smiling-african-american-student-in-glasses-using-digital-tablet-684x1024.jpg": {
		"pt-br": "Estudante afro-americano sorrindo usando tablet digital",
		"en": "Smiling African American student using a digital tablet",
		"es": "Estudiante afroamericano sonriente usando tableta digital",
	},
	"happy-african-american-couple-sitting-with-american-flag-and-baggage-in-departure-lounge-in-airport-1024x684.jpg": {
		"pt-br": "Casal feliz com bandeira americana e bagagem em lounge de aeroporto",
		"en": "Happy couple with American flag and luggage in airport departure lounge",
		"es": "Pareja feliz con bandera estadounidense y equipaje en sala de embarque",
	},
	"black-military-man-wrapped-in-flag-posing-with-wife-and-little-daughter-1024x683.jpg": {
		"pt-br": "Família com militar envolto na bandeira dos EUA posando com esposa e filha",
		"en": "Family with service member wrapped in U.S. flag posing with wife and daughter",
		"es": "Familia con militar envuelto en bandera de EE. UU. con esposa e hija",
	},
}

# slug da pasta (último segmento) -> og:image:alt por idioma (páginas de serviço)
OG_ALT_BY_SLUG: dict[str, dict[str, str]] = {
	"visto-de-trabalho": {
		"pt-br": "Visto de trabalho e autorização de emprego (EAD)",
		"en": "Work permit and employment authorization (EAD)",
		"es": "Permiso de trabajo y autorización de empleo (EAD)",
	},
	"work-permit": {
		"pt-br": "Visto de trabalho e autorização de emprego (EAD)",
		"en": "Work permit and employment authorization (EAD)",
		"es": "Permiso de trabajo y autorización de empleo (EAD)",
	},
	"permiso-de-trabajo": {
		"pt-br": "Visto de trabalho e autorização de emprego (EAD)",
		"en": "Work permit and employment authorization (EAD)",
		"es": "Permiso de trabajo y autorización de empleo (EAD)",
	},
	"documentos-de-viagem": {
		"pt-br": "Documentos de viagem para imigração",
		"en": "Immigration travel documents",
		"es": "Documentos de viaje para inmigración",
	},
	"travel-documents": {
		"pt-br": "Documentos de viagem para imigração",
		"en": "Immigration travel documents",
		"es": "Documentos de viaje para inmigración",
	},
	"documentos-de-viaje": {
		"pt-br": "Documentos de viagem para imigração",
		"en": "Immigration travel documents",
		"es": "Documentos de viaje para inmigración",
	},
	"peticao-familiar": {
		"pt-br": "Petição familiar de imigração",
		"en": "Family immigration petition",
		"es": "Petición familiar de inmigración",
	},
	"family-petitions": {
		"pt-br": "Petição familiar de imigração",
		"en": "Family immigration petition",
		"es": "Petición familiar de inmigración",
	},
	"ajuste-de-status": {
		"pt-br": "Ajuste de status para residência permanente",
		"en": "Adjustment of status to permanent residence",
		"es": "Ajuste de estatus a residencia permanente",
	},
	"adjustment-of-status": {
		"pt-br": "Ajuste de status para residência permanente",
		"en": "Adjustment of status to permanent residence",
		"es": "Ajuste de estatus a residencia permanente",
	},
	"ajuste-de-estatus": {
		"pt-br": "Ajuste de status para residência permanente",
		"en": "Adjustment of status to permanent residence",
		"es": "Ajuste de estatus a residencia permanente",
	},
	"processamento-consular": {
		"pt-br": "Processamento consular de visto de imigrante",
		"en": "Consular processing for immigrant visa",
		"es": "Procesamiento consular de visa de inmigrante",
	},
	"consular-processing": {
		"pt-br": "Processamento consular de visto de imigrante",
		"en": "Consular processing for immigrant visa",
		"es": "Procesamiento consular de visa de inmigrante",
	},
	"procesamiento-consular": {
		"pt-br": "Processamento consular de visto de imigrante",
		"en": "Consular processing for immigrant visa",
		"es": "Procesamiento consular de visa de inmigrante",
	},
	"naturalizacao": {
		"pt-br": "Naturalização e cidadania americana",
		"en": "Naturalization and U.S. citizenship",
		"es": "Naturalización y ciudadanía estadounidense",
	},
	"naturalization": {
		"pt-br": "Naturalização e cidadania americana",
		"en": "Naturalization and U.S. citizenship",
		"es": "Naturalización y ciudadanía estadounidense",
	},
	"naturalizacion": {
		"pt-br": "Naturalização e cidadania americana",
		"en": "Naturalization and U.S. citizenship",
		"es": "Naturalización y ciudadanía estadounidense",
	},
	"renovacao-de-residencia-i-90": {
		"pt-br": "Renovação de green card (Formulário I-90)",
		"en": "Green card renewal (Form I-90)",
		"es": "Renovación de green card (Formulario I-90)",
	},
	"residence-renewals-i-90": {
		"pt-br": "Renovação de green card (Formulário I-90)",
		"en": "Green card renewal (Form I-90)",
		"es": "Renovación de green card (Formulario I-90)",
	},
	"renovacion-de-residencia-i-90": {
		"pt-br": "Renovação de green card (Formulário I-90)",
		"en": "Green card renewal (Form I-90)",
		"es": "Renovación de green card (Formulario I-90)",
	},
	"waivers": {
		"pt-br": "Waiver de inadmissibilidade nos EUA",
		"en": "U.S. inadmissibility waiver",
		"es": "Waiver de inadmisibilidad en EE. UU.",
	},
	"vawa": {
		"pt-br": "Petição VAWA para vítimas de violência doméstica",
		"en": "VAWA petition for domestic violence survivors",
		"es": "Petición VAWA para víctimas de violencia doméstica",
	},
	"status-de-protecao-temporaria-tps": {
		"pt-br": "Status de Proteção Temporária (TPS)",
		"en": "Temporary Protected Status (TPS)",
		"es": "Estatus de Protección Temporal (TPS)",
	},
	"temporary-protected-status-tps": {
		"pt-br": "Status de Proteção Temporária (TPS)",
		"en": "Temporary Protected Status (TPS)",
		"es": "Estatus de Protección Temporal (TPS)",
	},
	"estatus-de-proteccion-temporal-tps": {
		"pt-br": "Status de Proteção Temporária (TPS)",
		"en": "Temporary Protected Status (TPS)",
		"es": "Estatus de Protección Temporal (TPS)",
	},
}
