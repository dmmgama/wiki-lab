---
title: Patrimônio — Schema Local (RULES)
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-003-topology-7namespaces.md"]
---

# RULES — patrimonio/

## Tags obrigatórias neste namespace

### `classe`
Classifica a natureza do activo ou tema patrimonial.

| Valor | Âmbito |
|---|---|
| `rendimento` | Fluxos de rendimento recorrente (rendas, dividendos, salários) |
| `imovel` | Imóveis — aquisição, gestão, valorização |
| `fiscal` | Planeamento fiscal, IRS, deduções, optimização |
| `investimento` | Carteiras, fundos, activos financeiros |

### `horizonte`
Horizonte temporal da decisão ou activo.

| Valor | Significado |
|---|---|
| `curto` | Horizonte < 2 anos |
| `longo` | Horizonte ≥ 2 anos |

## Exemplo de frontmatter completo
```yaml
---
title: Planeamento IRS 2026
status: research
confidence: medium
updated: 2026-04-10
provenance: ["AT", "patrimonio/"]
classe: fiscal
horizonte: curto
---
```

## Cross-links
Links para `work/` ou `familia/` permitidos quando relevante (ex: impacto fiscal de decisão profissional).
