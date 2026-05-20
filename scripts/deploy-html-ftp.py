#!/usr/bin/env python3
"""Envia arquivos .html (e .htaccess) para o FTP."""

from __future__ import annotations

import argparse
import ftplib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEPLOY_SUFFIXES = {".html", ".htaccess"}


def ensure_remote_dir(ftp: ftplib.FTP, remote_dir: str) -> None:
	parts = [p for p in remote_dir.strip("/").split("/") if p]
	path = ""
	for part in parts:
		path += f"/{part}"
		try:
			ftp.mkd(path)
		except ftplib.error_perm:
			pass


def load_env(path: Path) -> dict[str, str]:
	data: dict[str, str] = {}
	for line in path.read_text(encoding="utf-8").splitlines():
		line = line.strip()
		if not line or line.startswith("#") or "=" not in line:
			continue
		key, value = line.split("=", 1)
		data[key.strip()] = value.strip()
	return data


def git_changed_paths(since: str | None = None) -> list[Path]:
	"""Arquivos alterados (working tree + staged) ou desde um ref git."""
	seen: set[str] = set()
	commands: list[list[str]] = [
		["git", "diff", "--name-only"],
		["git", "diff", "--cached", "--name-only"],
	]
	if since:
		commands = [["git", "diff", "--name-only", since]]

	for cmd in commands:
		result = subprocess.run(
			cmd,
			cwd=ROOT,
			capture_output=True,
			text=True,
			check=False,
		)
		if result.returncode != 0:
			print(result.stderr or result.stdout, file=sys.stderr)
			sys.exit(1)
		for line in result.stdout.splitlines():
			line = line.strip()
			if line:
				seen.add(line)

	paths: list[Path] = []
	for rel in sorted(seen):
		p = ROOT / rel
		if p.suffix in DEPLOY_SUFFIXES and p.is_file():
			if "scripts" not in p.parts:
				paths.append(p)
	return paths


def collect_html_files(changed_only: bool, since: str | None) -> list[Path]:
	if changed_only or since:
		files = git_changed_paths(since)
		if not files:
			print("Nenhum arquivo .html/.htaccess alterado para enviar.")
		return files

	files = []
	for html in ROOT.rglob("*.html"):
		if "scripts" not in html.parts:
			files.append(html)
	return sorted(files)


def upload_files(files: list[Path], cfg: dict[str, str]) -> None:
	remote_base = cfg.get("FTP_REMOTE_DIR", "/public_html/").rstrip("/")

	ftp = ftplib.FTP()
	ftp.connect(cfg["FTP_HOST"], int(cfg.get("FTP_PORT", "21")), timeout=60)
	ftp.login(cfg["FTP_USER"], cfg["FTP_PASS"])
	ftp.set_pasv(True)

	for local in files:
		rel = local.relative_to(ROOT).as_posix()
		remote = f"{remote_base}/{rel}"
		ensure_remote_dir(ftp, str(Path(remote).parent))
		with local.open("rb") as handle:
			ftp.storbinary(f"STOR {remote}", handle)
		print(f"  {rel}")

	ftp.quit()
	print(f"Concluído: {len(files)} arquivo(s) enviado(s).")


def main() -> None:
	parser = argparse.ArgumentParser(description="Deploy HTML/.htaccess via FTP")
	parser.add_argument(
		"--changed",
		action="store_true",
		help="Envia só arquivos modificados no git (working tree + staged)",
	)
	parser.add_argument(
		"--since",
		metavar="REF",
		help="Envia arquivos alterados desde um commit/ref (ex: HEAD~1)",
	)
	args = parser.parse_args()

	env_path = ROOT / ".env"
	if not env_path.is_file():
		print("Arquivo .env não encontrado.", file=sys.stderr)
		sys.exit(1)

	files = collect_html_files(args.changed, args.since)
	if not files:
		return

	upload_files(files, load_env(env_path))


if __name__ == "__main__":
	main()
