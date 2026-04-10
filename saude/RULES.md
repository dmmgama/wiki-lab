---
title: Saúde — Schema Local (RULES)
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-003-topology-7namespaces.md"]
---

# RULES — saude/

## Tags obrigatórias neste namespace

### `eixo`
Classifica o eixo de saúde.

| Valor | Âmbito |
|---|---|
| `fisico` | Saúde física: diagnósticos, medicação, exercício, sono |
| `mental` | Saúde mental: estados, episódios, acompanhamento terapêutico |
| `rotina` | Rotinas e hábitos de bem-estar (alimentação, movimento, sono) |

## Nota de privacidade
Este namespace **nunca** é exposto publicamente. Conteúdo clínico não deve ser incluído em sessões de LLM sem revisão explícita.

## Princípio de entrada
Só entra conteúdo com valor de síntese (padrões, decisões, protocolos). Não entram consultas raw ou registos não sintetizados.

## Exemplo de frontmatter completo
```yaml
---
title: Protocolo de sono — optimização 2026
status: hypothesis
confidence: medium
updated: 2026-04-10
provenance: ["saude/", "reflexao-pessoal"]
eixo: rotina
---
```
