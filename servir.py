#!/usr/bin/env python3
"""Servidor HTTP para o espelho estático do newhopevisa.com."""

from __future__ import annotations

import http.server
import mimetypes
import os
import socketserver
import sys
from urllib.parse import parse_qs, urlsplit, urlunsplit

MIRROR_Q = "\uFE56"  # ﹖ (espelho HTTrack no lugar de ? em query strings)
ASSET_EXTS = {".css", ".js", ".woff", ".woff2", ".ttf", ".eot"}

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
ROOT = os.path.dirname(os.path.abspath(__file__))


class ReusableTCPServer(socketserver.TCPServer):
	allow_reuse_address = True


class Handler(http.server.SimpleHTTPRequestHandler):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, directory=ROOT, **kwargs)

	def _redirect(self, location: str) -> None:
		self.send_response(301)
		self.send_header("Location", location)
		self.end_headers()

	def _inject_head(self, body: bytes) -> bytes:
		if b"</head>" not in body:
			return body
		if b'id="local-dev-fix"' not in body:
			body = body.replace(
				b"</head>",
				b'<link rel="stylesheet" href="/local-fix.css" id="local-dev-fix" />\n</head>',
				1,
			)
		if b'id="local-url-clean"' not in body:
			body = body.replace(
				b"</head>",
				b'<script src="/local-redirect.js" id="local-url-clean"></script>\n</head>',
				1,
			)
		return body

	def _find_mirror_asset(self, clean_path: str, query: str) -> str | None:
		"""Mapeia reset.css?ver=3.4.5 → reset﹖ver=3.4.5.css no disco."""
		if not query:
			return None
		ver = parse_qs(query).get("ver", [None])[0]
		if not ver:
			return None
		base, ext = os.path.splitext(clean_path)
		if ext not in ASSET_EXTS:
			return None
		filename = f"{os.path.basename(base)}{MIRROR_Q}ver={ver}{ext}"
		candidate = os.path.join(os.path.dirname(self.translate_path(clean_path)), filename)
		return candidate if os.path.isfile(candidate) else None

	def _serve_file(self, path: str, send_body: bool) -> bool:
		if not os.path.isfile(path):
			return False
		ctype, _ = mimetypes.guess_type(path)
		if send_body:
			with open(path, "rb") as handle:
				data = handle.read()
			self.send_response(200)
			self.send_header("Content-Type", ctype or "application/octet-stream")
			self.send_header("Content-Length", str(len(data)))
			self.end_headers()
			self.wfile.write(data)
		else:
			self.send_response(200)
			self.send_header("Content-Type", ctype or "application/octet-stream")
			self.end_headers()
		return True

	def _serve_html_file(self, path: str) -> bool:
		if not os.path.isfile(path):
			return False
		with open(path, "rb") as handle:
			body = self._inject_head(handle.read())
		self.send_response(200)
		self.send_header("Content-Type", "text/html; charset=utf-8")
		self.send_header("Content-Length", str(len(body)))
		self.end_headers()
		self.wfile.write(body)
		return True

	def _resolve_request(self, send_body: bool) -> bool:
		"""Retorna True se a requisição foi atendida."""
		parsed = urlsplit(self.path)
		clean_path = parsed.path

		mirror = self._find_mirror_asset(clean_path, parsed.query)
		if mirror and self._serve_file(mirror, send_body):
			return True

		if clean_path.endswith("/index.html") or clean_path == "/index.html":
			target = clean_path[: -len("index.html")] or "/"
			self._redirect(urlunsplit(("", "", target, "", parsed.query)))
			return True

		if clean_path.endswith("/"):
			index_path = os.path.join(self.translate_path(clean_path), "index.html")
			if send_body and self._serve_html_file(index_path):
				return True
			if not send_body and os.path.isfile(index_path):
				self.send_response(200)
				self.send_header("Content-Type", "text/html; charset=utf-8")
				self.end_headers()
				return True

		if not os.path.splitext(clean_path)[1]:
			physical = self.translate_path(clean_path)
			if os.path.isdir(physical):
				self._redirect(
					urlunsplit(("", "", f"{clean_path.rstrip('/')}/", "", parsed.query))
				)
				return True
			index_path = os.path.join(physical, "index.html")
			if send_body and self._serve_html_file(index_path):
				return True
			if not send_body and os.path.isfile(index_path):
				self.send_response(200)
				self.send_header("Content-Type", "text/html; charset=utf-8")
				self.end_headers()
				return True

		if clean_path.endswith(".html") and os.path.isfile(self.translate_path(clean_path)):
			dir_path = os.path.dirname(clean_path)
			target = (dir_path + "/") if dir_path else "/"
			self._redirect(urlunsplit(("", "", target, "", parsed.query)))
			return True

		return False

	def do_GET(self):
		if not self._resolve_request(send_body=True):
			super().do_GET()

	def do_HEAD(self):
		if not self._resolve_request(send_body=False):
			super().do_HEAD()

	def log_message(self, fmt, *args):
		if args and str(args[1]).startswith("4"):
			super().log_message(fmt, *args)


def main() -> None:
	os.chdir(ROOT)
	with ReusableTCPServer(("", PORT), Handler) as httpd:
		print(f"Servidor: http://localhost:{PORT}/")
		print(f"  Português: http://localhost:{PORT}/pt-br/")
		print("Use servir.py (não python -m http.server) para URLs sem .html\n")
		try:
			httpd.serve_forever()
		except KeyboardInterrupt:
			print("\nServidor encerrado.")


if __name__ == "__main__":
	main()
