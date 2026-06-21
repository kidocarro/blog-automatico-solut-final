# Blog Solut — Routine (envio automático por email)

Routine de produção diária no Claude Code. Gera UM artigo (HTML + 2 imagens
Canva) e ENVIA automaticamente por email para dupanisson@gmail.com, com um
resumo do processo para conferência manual.

## Estrutura

```
solut-blog-routine/
├── temas.json          fila dos 30 temas
├── CLAUDE.md           instruções que o Claude segue a cada run
├── imagens/            PNGs exportados do Canva (capa.png, interna.png)
└── scripts/
    ├── run_pipeline.py pega o próximo tema da fila
    └── send_email.py   envia o email via SMTP do Gmail com anexos
```

## Setup (uma vez)

1. Suba este repositório no GitHub
2. Em claude.ai/code/routines, crie a Routine e conecte o repositório
3. Conecte o conector do **Canva**
4. Gere uma SENHA DE APP no Gmail da conta remetente:
   - Ative verificação em duas etapas (myaccount.google.com → Segurança)
   - Crie a senha em myaccount.google.com/apppasswords
5. Configure as variáveis de ambiente da Routine:
   - GMAIL_REMETENTE     = conta que envia (ex: contato@solut.com.br)
   - GMAIL_APP_PASSWORD  = senha de app de 16 caracteres
   - EMAIL_DESTINO       = dupanisson@gmail.com
6. Setup script: pip install requests
7. Trigger: Schedule diário no horário desejado
8. Prompt da Routine: "Siga o CLAUDE.md deste repositório para produzir o
   artigo do dia e enviar o email automaticamente."

## Importante

- O email é ENVIADO automaticamente, sem revisão antes do envio. O resumo do
  processo no corpo permite a conferência manual depois.
- A senha de app NUNCA vai no código nem em chat — só nas variáveis de
  ambiente da Routine.
- As imagens vão ANEXADAS ao email (PNG). Para publicar no site, baixe-as do
  email e suba na mídia do destino.

## Teste

Use Run now (não conta no limite diário). Confira se o email chegou em
dupanisson@gmail.com com o resumo, o artigo e as duas imagens anexadas.
