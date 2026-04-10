---
title: Meta — Schema Local (RULES)
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-003-topology-7namespaces.md"]
---

# RULES — meta/

## Tags obrigatórias neste namespace

### `tipo-meta`
Classifica a função do documento no sistema.

| Valor | Âmbito |
|---|---|
| `governance` | Políticas, regras, meta-schemas, namespaces-and-boundaries |
| `llm-context` | Contexto fornecido a agentes LLM (agents.md, registry, RULES.md) |
| `cross-link` | Índices ou mapas de relações entre namespaces |

### `revisao`
Ciclo de revisão recomendado.

| Formato | Exemplo |
|---|---|
| `YYYY-QN` | `2026-Q3` — revisão no 3.º trimestre de 2026 |

## Exemplo de frontmatter completo
```yaml
---
title: ADR-003 — Topologia 7 Namespaces
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-001", "handoff.md"]
tipo-meta: governance
revisao: 2026-Q4
---
```
