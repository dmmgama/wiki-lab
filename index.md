---
title: Wiki Lab — Índice Principal
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-001", "00-space-manual.md"]
---

# Wiki Lab — Índice

## Meta-ficheiros do projecto
- [00-space-manual.md](00-space-manual.md) — manual do Space, roadmap e regras de operação.
- [00-project-origin.md](00-project-origin.md) — origem, objectivo e restrições do projecto.
- [01-phase-1-knowledge-model.md](01-phase-1-knowledge-model.md) — perguntas e critérios da Fase 1.
- [02-open-questions.md](02-open-questions.md) — dúvidas e tensões em aberto.
- [agents.md](agents.md) — instruções para agentes LLM.
- [roadmap/ide-roadmap.md](roadmap/ide-roadmap.md) — fonte de verdade de execução.
- [handoff.md](handoff.md) — checkpoint vivo da última sessão.

## Namespaces

| Namespace | Pasta | Índice | Descrição |
|-----------|-------|--------|-----------|
| engineering | `engineering/` | [_index.md](engineering/_index.md) | Engenharia estrutural, Eurocódigos, SAP2000/ETABS |
| systems-ai | `systems-ai/` | [_index.md](systems-ai/_index.md) | Arquitectura wiki, agents, retrieval |
| personal | `personal/` | [_index.md](personal/_index.md) | Carreira, financeiro |
| shared | `shared/` | [_index.md](shared/_index.md) | Governance, ADRs transversais, registry |

## Conteúdo transversal

### Governance
- [governance/metadata-and-frontmatter.md](governance/metadata-and-frontmatter.md)
- [governance/namespaces-and-boundaries.md](governance/namespaces-and-boundaries.md)
- [governance/research-to-decision.md](governance/research-to-decision.md)

### Decisions
- [decisions/ADR-001-single-repo-with-namespaces.md](decisions/ADR-001-single-repo-with-namespaces.md)

### Foundations
- [foundations/00-what-is-an-llm-wiki.md](foundations/00-what-is-an-llm-wiki.md)

## Tooling
- [prompts/ide-implementation-001.md](prompts/ide-implementation-001.md) — prompt de implementação IDE.
- [shared/registry.md](shared/registry.md) — registry de namespaces.
- [templates/](templates/) — templates para research notes, wiki pages, ADRs, open questions.
- [scripts/validate.py](scripts/validate.py) — validação de frontmatter e links.

## Nota sobre estrutura
As pastas `governance/`, `decisions/` e `foundations/` permanecem na raiz. A topologia actual é navegável, validada e semanticamente clara. Migração física adiada indefinidamente — só justificável com benefício operacional explícito.
