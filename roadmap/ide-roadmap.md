---
title: Roadmap
status: decision
confidence: high
updated: 2026-04-10
provenance: ["00-space-manual.md", "agents.md", "prompts/ide-implementation-001.md", "meta/decisions/ADR-003-topology-7namespaces.md"]
---

# Roadmap

Este ficheiro é a fonte de verdade para o estado de execução do projecto.

## Fase actual
**Phase 2 — Refactor topologia + schemas locais** (concluída).

## Estado corrente (2026-04-10)

### Concluído
- Scaffold de namespaces criado: `engineering/`, `systems-ai/`, `personal/`, `shared/`. [Phase 1]
- Navegação: `index.md` raiz + `_index.md` por namespace + `shared/registry.md`. [Phase 1]
- Templates: `templates/` com 4 templates (research-note, wiki-page, adr, open-question). [Phase 1]
- Validação: `scripts/validate.py` — frontmatter, naming, links. 0 erros, 0 warnings. [Phase 1]
- Frontmatter YAML normalizado em todos os ficheiros. [Phase 1]
- Git inicializado, `.gitignore` criado, `README.md` criado. [Phase 1]
- Repo publicado em GitHub privado: https://github.com/dmmgama/wiki-lab.git (branch `main`). [Phase 1]
- ADR-001, ADR-002 criados e fechados. [Phase 1]
- **Phase 2 — Refactor topologia para 7 namespaces (Opção B):**
  - 7 namespaces criados: `work/`, `patrimonio/`, `familia/`, `relacoes/`, `saude/`, `dev-pessoal/`, `meta/`.
  - `engineering/` e `systems-ai/` movidos para `work/`.
  - `governance/` e `decisions/` movidos para `meta/`.
  - `foundations/` movido para `meta/foundations/`.
  - `personal/` removido (sem conteúdo a migrar).
  - RULES.md criados com schemas locais mínimos por namespace.
  - `RULES.md` raiz criado (schema universal).
  - `log.md` criado (registo cronológico).
  - `templates/namespace-rules.md` criado.
  - ADR-003 criado em `meta/decisions/`.
  - `shared/registry.md` actualizado com 7 namespaces + privacidade.
  - `index.md` raiz actualizado.
  - `02-open-questions.md` actualizado: Q-002, Q-006 com referência ao ADR-003.
  - `scripts/validate.py` actualizado: aceita `RULES.md` como nome válido.
  - Validação: **Erros: 0, Warnings: 0** (36 ficheiros).

### Questões fechadas
- Q-001 → `decided` (`meta/decisions/ADR-002-wiki-canonical-role.md`)
- Q-002 → `decided` (ADR-001 + ADR-003, topologia 7 namespaces)
- Q-003 → `decided` (`meta/governance/research-to-decision.md`)
- Q-004 → `decided` (`shared/registry.md`, `agents.md`)
- Q-006 → `decided` (`meta/governance/metadata-and-frontmatter.md`, RULES.md schemas)

### Em aberto
- Q-005 → `open`.
- Q-007 → `researching`.
- Q-008–Q-010 → `open`.

## Objectivo corrente
Criar conteúdo seed nos namespaces operacionais.

## Phase 1 — Validate and stabilize ✅
- Verify navigation and links. ✅
- Fix any validation warnings only if they affect correctness. ✅

## Phase 2 — Refactor topologia + schemas locais ✅
- Refatorar topologia para 7 namespaces (Opção B). ✅
- Criar RULES.md locais por namespace. ✅
- Criar templates/namespace-rules.md. ✅
- Criar ADR-003. ✅
- Actualizar registry, index, open-questions. ✅
- Validate: 0 erros, 0 warnings. ✅

## Phase 3 — Conteúdo seed
- Criar 1–2 páginas seed por namespace com frontmatter correcto.
- Começar pelos namespaces mais activos: `work/engineering/`, `work/systems-ai/`, `dev-pessoal/`.
- Validar que as tags locais (area, prioridade, etc.) são usadas correctamente.

## Phase 4 — Operational workflow
- Refinar templates se necessário.
- Melhorar validação (ex: validar tags locais por namespace).
- Pequenos scripts utilitários apenas se reduzem erro manual.

## Restrições
- Não introduzir migração adicional de pastas sem benefício operacional explícito.
- Não introduzir multi-wiki, routing semântico ou abstrações novas.
- Preferir simplicidade e auditabilidade.
- Namespaces privados (`familia/`, `relacoes/`, `saude/`) nunca expostos publicamente.

## Novos ficheiros desta sessão
- `work/index.md`, `work/RULES.md`
- `patrimonio/index.md`, `patrimonio/RULES.md`
- `familia/index.md`, `familia/RULES.md`
- `relacoes/index.md`, `relacoes/RULES.md`
- `saude/index.md`, `saude/RULES.md`
- `dev-pessoal/index.md`, `dev-pessoal/RULES.md`
- `meta/index.md`, `meta/RULES.md`
- `meta/decisions/ADR-003-topology-7namespaces.md`
- `RULES.md` (raiz), `log.md`
- `templates/namespace-rules.md`

## Próximo passo
Phase 3: criar conteúdo seed em `work/engineering/` ou `dev-pessoal/` com tags locais correctas.