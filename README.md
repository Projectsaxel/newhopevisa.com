# newhopevisa.com

Espelho estático do site [New Hope Immigration](https://newhopevisa.com) (WordPress/Elementor).

## Estrutura

- `/` — seletor de idioma
- `/pt-br/` — português
- `/en/` — inglês
- `/es/` — espanhol

## Desenvolvimento local

```bash
python3 servir.py
```

Abrir: http://localhost:8000/pt-br/

O `servir.py` resolve `arquivo.css?ver=X` → `arquivo﹖ver=X.css` (nomes do espelho HTTrack). Em produção, o `.htaccess` faz o mesmo no Apache.

## Deploy FTP (Hostinger)

Configure `.env` a partir de `.env.example` e execute:

```bash
python3 scripts/deploy-ftp.py
```

## Scripts

| Script | Uso |
|--------|-----|
| `servir.py` | Servidor local com URLs limpas e assets do espelho |
| `scripts/deploy-ftp.py` | Upload para produção |
| `scripts/restaurar-e-links-relativos.py` | Restaura HTML do site ao vivo e converte links |
| `scripts/urls-sem-html.py` | Remove `.html` dos links internos |
