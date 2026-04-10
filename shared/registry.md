---
title: Registry de Namespaces
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-001", "governance/namespaces-and-boundaries.md"]
---

# Registry de Namespaces

Este ficheiro lista todos os namespaces activos, a sua fronteira semântica e regras de escrita. Agentes devem consultar este registry para determinar onde ler ou escrever.

## Namespaces activos

| Namespace | Pasta | Fronteira | Regras de escrita |
|-----------|-------|-----------|-------------------|
| engineering | `engineering/` | Engenharia estrutural, Eurocódigos, SAP2000/ETABS | Apenas conteúdo técnico estrutural validado |
| systems-ai | `systems-ai/` | Wiki, agents, retrieval, knowledge mgmt | Apenas arquitectura e workflows do sistema |
| personal | `personal/` | Carreira, financeiro | Conteúdo prudente, sem exposição pública |
| shared | `shared/` | Governance, ADRs transversais, registry | Decisões e políticas que afectam todos os namespaces |

## Regras gerais
- Um agente escreve apenas no namespace que corresponde ao domínio da query.
- Se a query é ambígua entre namespaces, o agente deve questionar antes de escrever.
- Cross-links entre namespaces são permitidos mas explícitos e raros (max 5 por ficheiro).
- Conteúdo transversal (ADRs globais, governance) vai para `shared/`.

## Critérios de extração
Um namespace deve ser extraído para repo separado apenas se:
1. Pressão real de escala (>100 ficheiros), equipa (>1 pessoa) ou privacidade.
2. Ciclo de vida diverge significativamente do resto.
3. Custo de sincronização justifica separação física.

Posição actual: **adiada** — single-repo domina.
