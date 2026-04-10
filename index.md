---
title: Wiki Lab — Índice Principal
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-003-topology-7namespaces.md", "ADR-001", "00-space-manual.md"]
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
- [log.md](log.md) — registo cronológico de mudanças materiais.
- [RULES.md](RULES.md) — schema universal (meta-schema global).

## Namespaces

| Namespace | Pasta | Índice | Descrição |
|-----------|-------|--------|-----------|
| work | `work/` | [index.md](work/index.md) | Engenharia estrutural, carreira, sistemas, ferramentas |
| patrimonio | `patrimonio/` | [index.md](patrimonio/index.md) | Activos, imóveis, investimentos, fiscal |
| familia | `familia/` | [index.md](familia/index.md) | Co-parentalidade, Siena, dinâmicas familiares |
| relacoes | `relacoes/` | [index.md](relacoes/index.md) | Relações íntimas, amizades, profissionais |
| saude | `saude/` | [index.md](saude/index.md) | Saúde física, mental, rotinas |
| dev-pessoal | `dev-pessoal/` | [index.md](dev-pessoal/index.md) | Autoconhecimento, padrões, reflexão pessoal |
| meta | `meta/` | [index.md](meta/index.md) | Governance, ADRs, bases conceptuais do sistema |
| shared | `shared/` | [_index.md](shared/_index.md) | Registry de namespaces, utilitários transversais |

## Schemas locais
- [RULES.md](RULES.md) — schema universal (todos os namespaces).
- [work/RULES.md](work/RULES.md), [patrimonio/RULES.md](patrimonio/RULES.md), [familia/RULES.md](familia/RULES.md), [relacoes/RULES.md](relacoes/RULES.md), [saude/RULES.md](saude/RULES.md), [dev-pessoal/RULES.md](dev-pessoal/RULES.md), [meta/RULES.md](meta/RULES.md)

## Governance e Decisions
- [meta/governance/metadata-and-frontmatter.md](meta/governance/metadata-and-frontmatter.md)
- [meta/governance/namespaces-and-boundaries.md](meta/governance/namespaces-and-boundaries.md)
- [meta/governance/research-to-decision.md](meta/governance/research-to-decision.md)
- [meta/decisions/ADR-001-single-repo-with-namespaces.md](meta/decisions/ADR-001-single-repo-with-namespaces.md)
- [meta/decisions/ADR-002-wiki-canonical-role.md](meta/decisions/ADR-002-wiki-canonical-role.md)
- [meta/decisions/ADR-003-topology-7namespaces.md](meta/decisions/ADR-003-topology-7namespaces.md)

## Foundations
- [meta/foundations/00-what-is-an-llm-wiki.md](meta/foundations/00-what-is-an-llm-wiki.md)

## Tooling
- [prompts/ide-implementation-001.md](prompts/ide-implementation-001.md) — prompt de implementação IDE.
- [shared/registry.md](shared/registry.md) — registry de namespaces.
- [templates/](templates/) — templates para research notes, wiki pages, ADRs, RULES.md.
- [scripts/validate.py](scripts/validate.py) — validação de frontmatter e links.
