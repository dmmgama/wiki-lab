---
title: Família — Schema Local (RULES)
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-003-topology-7namespaces.md"]
---

# RULES — familia/

## Tags obrigatórias neste namespace

### `quem`
Identifica o elemento familiar relevante.

| Valor | Âmbito |
|---|---|
| `siena` | Filha Siena — desenvolvimento, saúde, escola, rotinas |
| `co-parent` | Questões de co-parentalidade, acordos, comunicação |

### `sensibilidade`
Nível de sensibilidade do conteúdo.

| Valor | Significado |
|---|---|
| `probatorio` | Conteúdo sensível (acordos legais, conflitos, documentação probatória) |
| `normal` | Conteúdo de rotina sem implicações legais ou relacionais delicadas |

## Nota de privacidade
Este namespace **nunca** é exposto publicamente. Conteúdo com `sensibilidade: probatorio` não deve ser incluído em sessões de LLM sem revisão explícita.

## Exemplo de frontmatter completo
```yaml
---
title: Rotina semanal Siena — 2026-Q2
status: decision
confidence: high
updated: 2026-04-10
provenance: ["familia/"]
quem: siena
sensibilidade: normal
---
```
