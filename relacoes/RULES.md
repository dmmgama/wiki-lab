---
title: Relações — Schema Local (RULES)
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-003-topology-7namespaces.md"]
---

# RULES — relacoes/

## Tags obrigatórias neste namespace

### `pessoa`
Identificador da pessoa ou par relacional. Usar nome ou pseudónimo consistente.

### `tipo-rel`
Classifica o tipo de relação.

| Valor | Âmbito |
|---|---|
| `intima` | Relações amorosas ou de parceria íntima |
| `amizade` | Amizades próximas com história ou profundidade |
| `profissional` | Relações profissionais com impacto no percurso pessoal |

## Nota de privacidade
Este namespace **nunca** é exposto publicamente. Conteúdo altamente sensível — seleccionar cuidadosamente o que entra aqui.

## Princípio de entrada
Só entra conteúdo com valor de síntese operacional (padrões, aprendizagens, decisões). Não entram transcrições ou registos brutos de conversas.

## Exemplo de frontmatter completo
```yaml
---
title: Padrão relacional — dinâmica de conflito e reparação
status: hypothesis
confidence: medium
updated: 2026-04-10
provenance: ["terapia", "reflexao-pessoal"]
pessoa: [identificador]
tipo-rel: intima
---
```
