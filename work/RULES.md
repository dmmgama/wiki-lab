---
title: Work — Schema Local (RULES)
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-003-topology-7namespaces.md"]
---

# RULES — work/

## Tags obrigatórias neste namespace

### `area`
Classifica o domínio de trabalho. Valor único por ficheiro.

| Valor | Âmbito |
|---|---|
| `jsj` | Empresa JSJ — projectos, clientes, processos internos |
| `carreira` | Desenvolvimento profissional, certificações, posicionamento |
| `competencia` | Técnicas e competências específicas (ex: betão pré-esforçado, EC8) |
| `ferramenta` | Software e ferramentas de trabalho (SAP2000, ETABS, VS Code) |

### `prioridade`
Urgência ou relevância operacional actual.

| Valor | Significado |
|---|---|
| `alta` | Acção necessária a curto prazo |
| `media` | Relevante, sem urgência imediata |
| `baixa` | Útil a longo prazo ou referência |

## Campos frontmatter adicionais permitidos
- `eurocode`: referência ao Eurocódigo relevante (ex: `"EC2"`, `"EC8"`).
- `software`: software de cálculo (ex: `"SAP2000"`, `"ETABS"`).

## Exemplo de frontmatter completo
```yaml
---
title: Dimensionamento de Vigas em Betão Pré-Esforçado
status: decision
confidence: high
updated: 2026-04-10
provenance: ["EC2", "work/engineering/"]
area: competencia
prioridade: alta
eurocode: EC2
---
```

## Cross-links
Links para outros namespaces permitidos mas explícitos e raros (max 5 por ficheiro).
