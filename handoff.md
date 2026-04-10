---
title: Handoff vivo
status: decision
confidence: high
updated: 2026-04-10
provenance: ["roadmap/ide-roadmap.md", "meta/decisions/ADR-003-topology-7namespaces.md"]
---

# Handoff — 2026-04-10

## Current state
Phase 2 concluída. Topologia refatorada para 7 namespaces operacionais (Opção B Claude). ADR-003 criado. Validação: **Erros: 0, Warnings: 0** (36 ficheiros).

**Repo:** https://github.com/dmmgama/wiki-lab.git  
**Branch:** `main`

## What changed this session
1. Topologia refatorada: 4 namespaces → 7 namespaces + `meta/` + `shared/`.
2. Movimentos de ficheiros (via `git mv`):
   - `engineering/` → `work/engineering/`
   - `systems-ai/` → `work/systems-ai/`
   - `governance/` → `meta/governance/`
   - `decisions/` → `meta/decisions/`
   - `foundations/` → `meta/foundations/`
   - `personal/` → removido (sem conteúdo útil)
3. Criados `index.md` + `RULES.md` para cada namespace (`work`, `patrimonio`, `familia`, `relacoes`, `saude`, `dev-pessoal`, `meta`).
4. Criado `RULES.md` raiz (schema universal).
5. Criado `log.md` raiz (registo cronológico).
6. Criado `templates/namespace-rules.md`.
7. Criado `meta/decisions/ADR-003-topology-7namespaces.md`.
8. Actualizado `shared/registry.md` com os 7 namespaces e flags de privacidade.
9. Actualizado `index.md` raiz com nova tabela de namespaces.
10. Actualizado `02-open-questions.md`: Q-002 e Q-006 com referência ao ADR-003.
11. Actualizado `scripts/validate.py`: regex de naming aceita `RULES.md`.
12. Links internos corrigidos em todos os ficheiros afectados.

## Open items
- Q-005 → `open`.
- Q-007 → `researching`.
- Q-008–Q-010 → `open`.

## Blockers
Nenhum.

## Next step
Phase 3: criar conteúdo seed nos namespaces.
- Começar por `work/engineering/` (1 página técnica) ou `dev-pessoal/` (1 padrão identificado).
- Usar as tags locais definidas nos RULES.md.

## Constraints
- Namespaces privados (`familia/`, `relacoes/`, `saude/`) nunca expostos publicamente nem incluídos em sessões LLM sem revisão explícita.
- Não introduzir novos namespaces sem benefício operacional demonstrado.
- Validação `scripts/validate.py` obrigatória antes de qualquer commit.

## Files updated this session
- `work/index.md`, `work/RULES.md`
- `work/engineering/_index.md`, `work/systems-ai/_index.md`
- `patrimonio/index.md`, `patrimonio/RULES.md`
- `familia/index.md`, `familia/RULES.md`
- `relacoes/index.md`, `relacoes/RULES.md`
- `saude/index.md`, `saude/RULES.md`
- `dev-pessoal/index.md`, `dev-pessoal/RULES.md`
- `meta/index.md`, `meta/RULES.md`
- `meta/decisions/ADR-003-topology-7namespaces.md`
- `meta/governance/` (movido de `governance/`)
- `meta/decisions/ADR-001, ADR-002` (movidos de `decisions/`)
- `meta/foundations/00-what-is-an-llm-wiki.md` (movido de `foundations/`)
- `RULES.md`, `log.md` (novos na raiz)
- `templates/namespace-rules.md`
- `shared/registry.md`, `shared/_index.md`
- `index.md`, `02-open-questions.md`
- `roadmap/ide-roadmap.md`, `scripts/validate.py`
- `handoff.md`

## Read first next session
1. `handoff.md` — este ficheiro.
2. `roadmap/ide-roadmap.md` — fase actual e próximo passo.
3. `meta/decisions/ADR-003-topology-7namespaces.md` — decisão desta sessão.