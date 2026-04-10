---
title: Registry de Namespaces
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-003-topology-7namespaces.md", "ADR-001", "meta/governance/namespaces-and-boundaries.md"]
---

# Registry de Namespaces

Este ficheiro lista todos os namespaces activos, a sua fronteira semântica e regras de escrita. Agentes devem consultar este registry para determinar onde ler ou escrever.

## Namespaces activos

| Namespace | Pasta | Fronteira | RULES | Regras de escrita |
|-----------|-------|-----------|-------|-------------------|
| work | `work/` | Trabalho profissional: engenharia estrutural, carreira, sistemas, ferramentas | [work/RULES.md](../work/RULES.md) | Tags: `area`, `prioridade` |
| patrimonio | `patrimonio/` | Activos, imóveis, investimentos, planeamento fiscal | [patrimonio/RULES.md](../patrimonio/RULES.md) | Tags: `classe`, `horizonte` |
| familia | `familia/` | Co-parentalidade, Siena, dinâmicas familiares | [familia/RULES.md](../familia/RULES.md) | Tags: `quem`, `sensibilidade`. Nunca exposto publicamente |
| relacoes | `relacoes/` | Relações íntimas, amizades, profissionais relevantes | [relacoes/RULES.md](../relacoes/RULES.md) | Tags: `pessoa`, `tipo-rel`. Nunca exposto publicamente |
| saude | `saude/` | Saúde física, mental, rotinas | [saude/RULES.md](../saude/RULES.md) | Tag: `eixo`. Nunca exposto publicamente |
| dev-pessoal | `dev-pessoal/` | Autoconhecimento, padrões, reflexão pessoal | [dev-pessoal/RULES.md](../dev-pessoal/RULES.md) | Tags: `padrao`, `fonte` |
| meta | `meta/` | Governance, ADRs, bases conceptuais do sistema | [meta/RULES.md](../meta/RULES.md) | Tags: `tipo-meta`, `revisao`. Apenas decisões e governance |
| shared | `shared/` | Registry de namespaces, utilitários transversais | — | Políticas que afectam todos os namespaces |

## Regras gerais
- Um agente escreve apenas no namespace que corresponde ao domínio da query.
- Se a query é ambígua entre namespaces, o agente deve questionar antes de escrever.
- Cross-links entre namespaces são permitidos mas explícitos e raros (max 5 por ficheiro).
- Conteúdo transversal (ADRs globais, governance) vai para `meta/`.
- Schema universal em [RULES.md](../RULES.md) raiz.

## Namespaces privados (nunca expor publicamente)
- `familia/`
- `relacoes/`
- `saude/`

## Critérios de extração
Um namespace deve ser extraído para repo separado apenas se:
1. Pressão real de escala (>100 ficheiros), equipa (>1 pessoa) ou privacidade.
2. Ciclo de vida diverge significativamente do resto.
3. Custo de sincronização justifica separação física.

Posição actual: **adiada** — single-repo domina (ADR-001).
