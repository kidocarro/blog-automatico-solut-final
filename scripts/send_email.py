#!/usr/bin/env python3
"""
send_email.py — envia o artigo do dia por email via SMTP do Gmail.

Uso:
    python scripts/send_email.py \
        --assunto "Artigo do dia: ..." \
        --corpo-html corpo.html \
        --imagens imagens/capa.png imagens/interna.png

Variáveis de ambiente esperadas (configurar na Routine):
    GMAIL_REMETENTE     conta que envia (ex: contato@solut.com.br)
    GMAIL_APP_PASSWORD  senha de app de 16 caracteres gerada no Google
    EMAIL_DESTINO       destinatário (ex: dupanisson@gmail.com)

O corpo é HTML (resumo do processo + artigo). As imagens vão anexadas.
"""

import argparse
import os
import smtplib
import sys
from email.message import EmailMessage
from pathlib import Path

REMETENTE = os.environ["GMAIL_REMETENTE"]
APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]
DESTINO = os.environ.get("EMAIL_DESTINO", "dupanisson@gmail.com")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465  # SSL


def enviar(assunto: str, corpo_html_path: str, imagens: list[str]) -> None:
    msg = EmailMessage()
    msg["Subject"] = assunto
    msg["From"] = REMETENTE
    msg["To"] = DESTINO

    with open(corpo_html_path, "r", encoding="utf-8") as f:
        corpo_html = f.read()

    # Versão texto simples (fallback) + versão HTML
    msg.set_content(
        "Este email contém o resumo do processo e o artigo do dia em HTML. "
        "Abra em um cliente compatível com HTML para visualizar."
    )
    msg.add_alternative(corpo_html, subtype="html")

    # Anexa as imagens
    for caminho in imagens:
        p = Path(caminho)
        if not p.exists():
            print(f"AVISO: imagem não encontrada, pulando: {caminho}")
            continue
        with open(p, "rb") as img:
            dados = img.read()
        msg.add_attachment(
            dados,
            maintype="image",
            subtype="png",
            filename=p.name,
        )

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as servidor:
        servidor.login(REMETENTE, APP_PASSWORD)
        servidor.send_message(msg)

    print(f"EMAIL_ENVIADO_OK para={DESTINO} assunto={assunto!r}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--assunto", required=True)
    parser.add_argument("--corpo-html", required=True)
    parser.add_argument("--imagens", nargs="*", default=[])
    args = parser.parse_args()
    enviar(args.assunto, args.corpo_html, args.imagens)


if __name__ == "__main__":
    main()
