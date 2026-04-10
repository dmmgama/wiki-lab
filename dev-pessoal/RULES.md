---
title: Desenvolvimento Pessoal — Schema Local (RULES)
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-003-topology-7namespaces.md"]
---

# RULES — dev-pessoal/

## Tags obrigatórias neste namespace

### `padrao`
Nome ou descrição curta do padrão identificado (texto livre, snake_case).

Exemplos: `evitamento_conflito`, `perfeccionismo_bloqueante`, `necessidade_validacao`.

### `fonte`
Origem da identificação do padrão.

| Valor | Âmbito |
|---|---|
| `terapia` | Identificado em contexto terapêutico |
| `reflexao` | Reflexão pessoal autónoma |
| `incidente` | Emergiu de um incidente ou situação concreta |

## Exemplo de frontmatter completo
```yaml
---
title: Padrão — dificuldade de delegação sob pressão
status: hypothesis
confidence: medium
updated: 2026-04-10
provenance: ["dev-pessoal/", "terapia"]
padrao: dificuldade_delegacao
fonte: terapia
---
```

## Cross-links
Padrões com impacto relacional podem linkar para `relacoes/`. Padrões com impacto profissional podem linkar para `work/`.
