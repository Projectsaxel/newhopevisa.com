#!/usr/bin/env python3
"""Envia apenas arquivos .html (rápido após correções pontuais)."""

from __future__ import annotations

import ftplib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


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


def main() -> None:
	env_path = ROOT / ".env"
	if not env_path.is_file():
		print("Arquivo .env não encontrado.", file=sys.stderr)
		sys.exit(1)
	cfg = load_env(env_path)
	remote_base = cfg.get("FTP_REMOTE_DIR", "/public_html/").rstrip("/")

	ftp = ftplib.FTP()
	ftp.connect(cfg["FTP_HOST"], int(cfg.get("FTP_PORT", "21")), timeout=60)
	ftp.login(cfg["FTP_USER"], cfg["FTP_PASS"])
	ftp.set_pasv(True)

	count = 0
	for html in ROOT.rglob("*.html"):
		if "scripts" in html.parts:
			continue
		rel = html.relative_to(ROOT).as_posix()
		remote = f"{remote_base}/{rel}"
		ensure_remote_dir(ftp, str(Path(remote).parent))
		with html.open("rb") as handle:
			ftp.storbinary(f"STOR {remote}", handle)
		count += 1
		print(f"  {rel}")
	ftp.quit()
	print(f"Concluído: {count} HTML enviados.")


if __name__ == "__main__":
	main()
