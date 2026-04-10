---
title: Metadata e Frontmatter Mínimos
status: decision
phase: 1
confidence: high
updated: 2026-04-10
provenance: ["01-phase-1", "Q-006"]
---

# Meta-Schema Mínimo

Todos os ficheiros usam YAML frontmatter delimitado por `---`. Máximo 15 linhas; campos inline onde possível.

## Campos Obrigatórios (Todos Namespaces)
- `title`: Título único, descritivo (<80 chars).
- `status`: Enum (frontmatter): `research`, `hypothesis`, `decision`, `dropped`, `implemented`.
  - Nota: `02-open-questions.md` usa enum próprio: `open`, `researching`, `decided`, `dropped`.
- `confidence`: Enum: `low`, `medium`, `high`; grau de certeza factual.
- `updated`: ISO date (YYYY-MM-DD).
- `provenance`: Array de strings; origens (e.g., "Q-001", "chat-2026-04-10", "source:URL").

Exemplo mínimo:

title: Exemplo Ficheiro
status: research
confidence: medium
updated: 2026-04-10
provenance: ["Q-003", "NotebookLM-001"]


## Campos Variáveis por Namespace
- Namespaces definem schemas locais via ficheiro `namespace/schema.md`.
- Extras comuns: `namespace`, `related: ["ficheiro1.md"]`, `sources: [URL1, URL2]`.
- Engineering: Adicionar `eurocode: "EC2"`, `software: "SAP2000"`.
- Sem campos livres; validar contra schema local.

## Regras de Provenance e Tracking
- `provenance` liga a open-questions, ADRs, chats ou fontes externas.
- `confidence` baixa se >30% hipóteses não testadas.
- Timestamps: `updated` manual; Git commit como layer extra.
- Dropped: Manter ficheiro com `status: dropped`; linkar de `02-open-questions.md`.

## Validação de Consistência
- Script Python local: Verificar frontmatter parseável, campos obrigatórios presentes, enum válidos.
- Sem schema JSON gigante; validar por namespace via regex/YAML lint.
- Workflow: Pre-commit hook no Git repo principal.