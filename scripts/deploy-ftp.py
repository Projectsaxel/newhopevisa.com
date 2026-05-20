#!/usr/bin/env python3
"""Envia o espelho estático para o FTP (Hostinger)."""

from __future__ import annotations

import ftplib
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "scripts", "__pycache__", ".cursor"}
SKIP_FILES = {
	".env",
	".env.example",
	".gitignore",
	"servir.py",
	"iniciar.sh",
	".DS_Store",
}


def load_env(path: Path) -> dict[str, str]:
	data: dict[str, str] = {}
	for line in path.read_text(encoding="utf-8").splitlines():
		line = line.strip()
		if not line or line.startswith("#") or "=" not in line:
			continue
		key, value = line.split("=", 1)
		data[key.strip()] = value.strip()
	return data


def ensure_remote_dir(ftp: ftplib.FTP, remote_dir: str) -> None:
	parts = [p for p in remote_dir.strip("/").split("/") if p]
	path = ""
	for part in parts:
		path += f"/{part}"
		try:
			ftp.mkd(path)
		except ftplib.error_perm:
			pass


def upload_tree(ftp: ftplib.FTP, local_root: Path, remote_base: str) -> tuple[int, int]:
	uploaded = 0
	skipped = 0
	remote_base = remote_base.rstrip("/")

	for dirpath, dirnames, filenames in os.walk(local_root):
		dirnames[:] = [
			d
			for d in dirnames
			if d not in SKIP_DIRS and not d.startswith(".")
		]
		local_dir = Path(dirpath)
		rel = local_dir.relative_to(local_root)
		remote_dir = remote_base if rel == Path(".") else f"{remote_base}/{rel.as_posix()}"
		ensure_remote_dir(ftp, remote_dir)

		for name in filenames:
			if name in SKIP_FILES or name.startswith("."):
				skipped += 1
				continue
			local_file = local_dir / name
			remote_file = f"{remote_dir}/{name}"
			with local_file.open("rb") as handle:
				ftp.storbinary(f"STOR {remote_file}", handle)
			uploaded += 1
			if uploaded % 25 == 0:
				print(f"  {uploaded} arquivos enviados…")

	return uploaded, skipped


def main() -> None:
	env_path = ROOT / ".env"
	if not env_path.is_file():
		print("Arquivo .env não encontrado.", file=sys.stderr)
		sys.exit(1)

	cfg = load_env(env_path)
	host = cfg["FTP_HOST"]
	port = int(cfg.get("FTP_PORT", "21"))
	user = cfg["FTP_USER"]
	password = cfg["FTP_PASS"]
	remote_dir = cfg.get("FTP_REMOTE_DIR", "/public_html/")

	print(f"Conectando em {host}:{port}…")
	ftp = ftplib.FTP()
	ftp.connect(host, port, timeout=60)
	ftp.login(user, password)
	ftp.set_pasv(True)

	print(f"Enviando para {remote_dir} …")
	uploaded, skipped = upload_tree(ftp, ROOT, remote_dir)
	ftp.quit()

	print(f"Concluído: {uploaded} enviados, {skipped} ignorados localmente.")


if __name__ == "__main__":
	main()
