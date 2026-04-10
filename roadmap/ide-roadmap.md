---
title: Roadmap
status: decision
confidence: high
updated: 2026-04-10
provenance: ["00-space-manual.md", "agents.md", "prompts/ide-implementation-001.md"]
---

# Roadmap

Este ficheiro é a fonte de verdade para o estado de execução do projecto.

## Fase actual
**Phase 1 — Validate and stabilize** (concluída).

## Estado corrente (2026-04-10)

### Concluído
- Scaffold de namespaces criado: `engineering/`, `systems-ai/`, `personal/`, `shared/`.
- Navegação: `index.md` raiz + `_index.md` por namespace + `shared/registry.md`.
- Templates: `templates/` com 4 templates (research-note, wiki-page, adr, open-question).
- Validação: `scripts/validate.py` — frontmatter, naming, links. 0 erros, 0 warnings.
- Frontmatter YAML normalizado em todos os ficheiros (19 validados).
- Enum `status` uniformizado: `decision` (não `decided`) no frontmatter, com nota sobre enum próprio em open-questions (`open/researching/decided/dropped`).
- `agents.md` actualizado com regras de arranque, persistência, handoff e roadmap.
- `00-space-manuald.md` removido (versão antiga pré-ADR-001).
- Decisão: **não migrar pastas** (`governance/`, `decisions/`, `foundations/` permanecem na raiz). Topologia actual é definitiva até justificação operacional.

### Questões fechadas
- Q-002 → `decided` (ADR-001, namespaces-and-boundaries.md)
- Q-003 → `decided` (research-to-decision.md)
- Q-004 → `decided` (shared/registry.md, agents.md)
- Q-006 → `decided` (metadata-and-frontmatter.md, namespaces-and-boundaries.md)

### Em aberto
- Q-001 — papel canónico da wiki → `researching` (foundations cobre parcialmente, falta ADR).
- Q-005, Q-007–Q-010 → `open`.

## Objectivo corrente
Implementar a primeira camada operacional do repo sem alterar arquitectura.

## Phase 1 — Validate and stabilize ✅
- Verify navigation and links. ✅
- Keep top-level folders as-is. ✅
- Fix any validation warnings only if they affect correctness. ✅
- Do not migrate folders. ✅ (decisão final)

## Phase 2 — Add content
- Create first content pages inside namespaces.
- Add one or two seed pages per namespace.
- Close Q-001 with ADR if needed.

## Phase 3 — Operational workflow
- Refine templates.
- Improve validation if necessary.
- Add small utility scripts only if they reduce manual error.

## Restrições
- Não mexer na topologia sem benefício operacional explícito.
- Não introduzir migração de pastas, multi-wiki, routing semântico ou abstrações novas.
- Preferir simplicidade e auditabilidade.

## Próximo passo
Opção A: criar conteúdo seed nos namespaces (1–2 páginas por namespace).
Opção B: fechar Q-001 com ADR formal sobre o papel canónico da wiki.