---
title: Handoff vivo
status: decision
confidence: high
updated: 2026-04-10
provenance: ["roadmap/ide-roadmap.md", "agents.md"]
---

# Handoff — 2026-04-10

## Current state
Phase 1 (Validate and stabilize) concluída. Repo inicializado em Git, publicado em GitHub privado. 26 ficheiros committed, 0 erros de validação.

**Repo:** https://github.com/dmmgama/wiki-lab.git
**Branch:** `main`

## What changed this session
1. Scaffold completo de namespaces: `engineering/`, `systems-ai/`, `personal/`, `shared/` com `_index.md`.
2. `index.md` raiz como ponto de entrada de navegação.
3. `shared/registry.md` com namespaces e regras de escrita.
4. `templates/` com 4 templates (research-note, wiki-page, adr, open-question).
5. `scripts/validate.py` — validação frontmatter, naming, links. SKIP_FILES: README.md, AGENTS.md, LICENSE.
6. Frontmatter YAML adicionado a todos os ficheiros Markdown do projecto.
7. Enum `status` uniformizado (`decision`, não `decided`).
8. `provenance` adicionado onde faltava.
9. `agents.md` com regras completas (arranque, persistência, handoff, roadmap, GitHub Copilot adenda).
10. `00-space-manuald.md` removido (versão antiga).
11. Decisão: **não migrar pastas** — topologia actual é definitiva.
12. Q-002, Q-003, Q-004, Q-006 → `decided`.
13. `.gitignore` criado (Python, IDE, OS).
14. `README.md` criado (GitHub-facing).
15. Git init, commit inicial (26 ficheiros), push para GitHub privado `dmmgama/wiki-lab`.
16. `gh` CLI instalado via winget.

## Open items
- Q-001: papel canónico da wiki → `researching`.
- Q-005: papel do NotebookLM → `open`.
- Q-007: wiki-lab como conceito → `researching`.
- Q-008–Q-010 → `open`.

## Blockers
Nenhum.

## Next step
Opção A: criar conteúdo seed — `engineering/eurocodes.md` (Eurocódigos síntese, status:decision).
Opção B: fechar Q-001 com ADR formal sobre o papel canónico da wiki.

## Constraints
- Não mexer na topologia sem benefício operacional explícito.
- Não introduzir migração, multi-wiki, routing semântico ou abstrações novas.

## Files updated this session
- Todos os ficheiros do repo (scaffold + frontmatter + validação).
- `.gitignore` (criado)
- `README.md` (criado)
- `handoff.md` (sobrescrito)
- `roadmap/ide-roadmap.md` (actualizado)

## Read first next session
1. `handoff.md` — este ficheiro.
2. `roadmap/ide-roadmap.md` — fonte de verdade de execução.
3. `index.md` — navegação raiz.
3. `index.md` — navegação do repo.