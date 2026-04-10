---
title: Handoff vivo
status: decision
confidence: high
updated: 2026-04-10
provenance: ["roadmap.md", "agents.md"]
---

# Handoff — 2026-04-10

## Current state
Phase 1 (Validate and stabilize) concluída. Repo scaffold completo, validado, navegável. 16 ficheiros com frontmatter, 0 erros, 0 warnings.

## What changed this session
1. Scaffold de namespaces criado: `engineering/`, `systems-ai/`, `personal/`, `shared/` com `_index.md`.
2. `index.md` raiz criado como ponto de entrada.
3. `shared/registry.md` criado com lista de namespaces e regras de escrita.
4. `templates/` criado com 4 templates (research-note, wiki-page, adr, open-question).
5. `scripts/validate.py` criado — validação de frontmatter, naming, links internos.
6. Frontmatter YAML adicionado a 8 ficheiros pré-existentes que não tinham.
7. Enum `status` uniformizado: `decided` → `decision` nos frontmatter de governance.
8. `provenance` adicionado onde faltava.
9. `agents.md` actualizado com regras completas (arranque, persistência, handoff, roadmap).
10. `00-space-manuald.md` removido (versão antiga).
11. Decisão final: **não migrar pastas** — topologia actual é definitiva.
12. Q-002, Q-003, Q-004, Q-006 marcadas como `decided` com referências explícitas.
13. Q-001 mantida em `researching`.
14. `roadmap.md` criado na raiz como fonte de verdade de execução.
15. `roadmap/ide-roadmap.md` actualizado com estado completo.
16. Notas de "migração futura" removidas de index.md e _index.md.

## Open items
- Q-001: papel canónico da wiki → `researching` (foundations cobre parcialmente, falta ADR formal).
- Q-005: papel do NotebookLM → `open`.
- Q-007: wiki-lab como conceito → `researching`.
- Q-008: stack mínima → `open`.
- Q-009: modelo visual → `open`.
- Q-010: compreensão antes de commitment → `open`.

## Blockers
Nenhum.

## Next step
Opção A: criar conteúdo seed nos namespaces (1–2 páginas por namespace).
Opção B: fechar Q-001 com ADR formal sobre o papel canónico da wiki.

## Constraints
- Não mexer na topologia sem benefício operacional explícito.
- Não introduzir migração de pastas, multi-wiki, routing semântico ou abstrações novas.

## Files updated this session
- `agents.md` (editado)
- `02-open-questions.md` (editado)
- `governance/metadata-and-frontmatter.md` (editado)
- `governance/research-to-decision.md` (editado)
- `governance/namespaces-and-boundaries.md` (editado)
- `decisions/ADR-001-single-repo-with-namespaces.md` (editado)
- `foundations/00-what-is-an-llm-wiki.md` (editado)
- `00-project-origin.md` (editado)
- `00-space-manual.md` (editado)
- `01-phase-1-knowledge-model.md` (editado)
- `index.md` (criado)
- `engineering/_index.md` (criado)
- `systems-ai/_index.md` (criado)
- `personal/_index.md` (criado)
- `shared/_index.md` (criado)
- `shared/registry.md` (criado)
- `templates/research-note.md` (criado)
- `templates/wiki-page.md` (criado)
- `templates/adr.md` (criado)
- `templates/open-question.md` (criado)
- `scripts/validate.py` (criado)
- `roadmap.md` (criado)
- `roadmap/ide-roadmap.md` (editado)
- `handoff.md` (sobrescrito)
- `00-space-manuald.md` (removido)

## Read first next session
1. `handoff.md` — este ficheiro.
2. `roadmap/ide-roadmap.md` — fonte de verdade de execução.
3. `index.md` — navegação do repo.