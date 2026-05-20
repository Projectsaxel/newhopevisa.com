#!/bin/bash
cd "$(dirname "$0")"
echo "Iniciando servidor em http://localhost:8000/pt-br/"
echo "Pressione Ctrl+C para parar."
exec python3 servir.py 8000
