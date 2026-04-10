---
title: RULES — Schema Universal
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-003-topology-7namespaces.md", "governance/metadata-and-frontmatter.md"]
---

# RULES — Schema Universal

Este ficheiro define o meta-schema mínimo obrigatório para **todos** os ficheiros Markdown do repositório. Cada namespace pode ter um `RULES.md` local com campos adicionais.

## Frontmatter obrigatório (todos os namespaces)

```yaml
---
title: [string, descritivo e único no namespace]
status: [research | hypothesis | decision | dropped | implemented]
confidence: [low | medium | high]
updated: [YYYY-MM-DD]
provenance: [lista de fontes — ficheiros, ADRs, referências externas]
---
```

## Enums válidos

### `status`
| Valor | Significado |
|---|---|
| `research` | Exploração em curso; conteúdo volátil |
| `hypothesis` | Hipótese formulada; incerteza explícita |
| `decision` | Decisão fechada; estável |
| `dropped` | Abandonado; não apagado — mantido para auditabilidade |
| `implemented` | Materializou-se em artefacto operacional |

### `confidence`
| Valor | Significado |
|---|---|
| `low` | Muita incerteza; entrada recente |
| `medium` | Razoavelmente fundamentado |
| `high` | Consolidado, revisto, estável |

## Convenções de naming
- Ficheiros: `lowercase-hyphens.md` (ex: `decisao-fiscal-2026.md`).
- Excepções aceites: `_index.md`, `ADR-NNN-*.md`, `RULES.md`, `README.md`.
- Sem espaços, sem acentos nos nomes de ficheiro.

## Provenance
Campo obrigatório. Lista de strings com fontes da informação:
- Ficheiros internos: `"decisions/ADR-001.md"` 
- Referências externas: `"EC2"`, `"DSM-5"`
- Experiências/processos: `"terapia"`, `"reflexao-pessoal"`

## Schemas locais por namespace
Cada namespace tem um `RULES.md` local com tags adicionais obrigatórias dentro desse namespace:

| Namespace | RULES | Tags locais |
|---|---|---|
| `work/` | [work/RULES.md](work/RULES.md) | `area`, `prioridade` |
| `patrimonio/` | [patrimonio/RULES.md](patrimonio/RULES.md) | `classe`, `horizonte` |
| `familia/` | [familia/RULES.md](familia/RULES.md) | `quem`, `sensibilidade` |
| `relacoes/` | [relacoes/RULES.md](relacoes/RULES.md) | `pessoa`, `tipo-rel` |
| `saude/` | [saude/RULES.md](saude/RULES.md) | `eixo` |
| `dev-pessoal/` | [dev-pessoal/RULES.md](dev-pessoal/RULES.md) | `padrao`, `fonte` |
| `meta/` | [meta/RULES.md](meta/RULES.md) | `tipo-meta`, `revisao` |
