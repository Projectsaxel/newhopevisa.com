#!/usr/bin/env python3
"""Corrige lang, og:locale e inLanguage em en/, es/ e pt-br/."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

LOCALE = {
	"pt-br": ("pt-BR", "pt_BR"),
	"en": ("en", "en_US"),
	"es": ("es", "es_ES"),
}

TWITTER_ES = {
	"Escrito por": "Escrito por",
	"Tempo para leitura": "Tiempo de lectura",
	"minuto": "minuto",
	"minutos": "minutos",
}
TWITTER_EN = {
	"Tempo para leitura": "Reading time",
	"Escrito por": "Written by",
	"minuto": "minute",
	"minutos": "minutes",
}
TWITTER_PT = TWITTER_ES  # pt-br keeps Portuguese labels


def lang_from_path(path: Path) -> str | None:
	parts = path.relative_to(ROOT).parts
	if len(parts) >= 1 and parts[0] in LOCALE:
		return parts[0]
	return None


def patch_file(path: Path) -> bool:
	lang_key = lang_from_path(path)
	if not lang_key:
		return None
	html_lang, og_locale = LOCALE[lang_key]
	text = path.read_text(encoding="utf-8")
	orig = text

	text = re.sub(r'<html lang="[^"]*"', f'<html lang="{html_lang}"', text, count=1)
	text = text.replace('content="pt_BR"', f'content="{og_locale}"')
	text = text.replace('"inLanguage":"pt-BR"', f'"inLanguage":"{html_lang}"')
	text = text.replace('"inLanguage": "pt-BR"', f'"inLanguage": "{html_lang}"')

	if lang_key == "es":
		text = text.replace(
			"Otimização dos mecanismos de pesquisa pelo Rank Math PRO",
			"Optimización para motores de búsqueda por Rank Math PRO",
		)
		text = text.replace("Ir para o conteúdo", "Ir al contenido")
		text = text.replace("Feed para New Hope", "Feed de New Hope")
		text = text.replace("Feed de comentários para New Hope", "Feed de comentarios de New Hope")
		for old, new in TWITTER_ES.items():
			text = text.replace(old, new)
	elif lang_key == "en":
		text = text.replace(
			"Otimização dos mecanismos de pesquisa pelo Rank Math PRO",
			"Search engine optimization by Rank Math PRO",
		)
		text = text.replace("Ir para o conteúdo", "Skip to content")
		text = text.replace("Feed para New Hope", "New Hope Feed")
		text = text.replace("Feed de comentários para New Hope", "New Hope Comments Feed")
		for old, new in TWITTER_EN.items():
			text = text.replace(old, new)

	if text != orig:
		path.write_text(text, encoding="utf-8")
		return True
	return False


def main() -> None:
	n = 0
	for html in sorted(ROOT.rglob("index.html")):
		if "scripts" in html.parts:
			continue
		if patch_file(html):
			n += 1
	print(f"Arquivos com lang/locale corrigidos: {n}")


if __name__ == "__main__":
	main()
