---
title: Instruções para Agentes
status: decision
confidence: high
updated: 2026-04-10
provenance: ["00-space-manual.md", "ADR-001"]
---

# Instruções para Agentes

## Objetivo
Este repositório é um sistema de knowledge management baseado num único repo com namespaces por domínio, Markdown como formato canónico, governance explícita e separação clara entre research, curated wiki, decisões e implementação.

## Arranque obrigatório
Antes de qualquer trabalho, ler:
- `00-space-manual.md`
- `00-project-origin.md`
- `01-phase-1-knowledge-model.md`
- `02-open-questions.md`
- `index.md` — índice de navegação raiz.
- `shared/registry.md` — registry de namespaces e regras de escrita.
- `roadmap/ide-roadmap.md` — fonte de verdade de execução.
- `handoff.md` — checkpoint vivo da sessão anterior.

Depois:
- reconstruir a fase atual do projeto;
- identificar o namespace relevante (consultar `shared/registry.md`);
- identificar se a tarefa é research, hipótese, decisão ou implementação;
- validar se o `handoff.md` e o roadmap batem certo com o estado real do repo.

## Distinções imperativas
- **Research**: exploração, comparação, levantamento; pode ser volátil.
- **Hipótese**: incerteza explícita; registar em `02-open-questions.md` quando relevante.
- **Decisão**: escolha fechada; registar em ADR.
- **Implementação**: materialização da decisão; nunca antecipar sem decisão suficiente.

## Regras operacionais
- Responder em PT por defeito.
- Usar tom técnico, direto e sem fluff.
- Quando relevante, começar com BLUF.
- Enunciar pressupostos numerados quando existirem.
- Quando houver decisão, apresentar 2–4 opções com trade-offs e posição recomendada.
- Preferir a solução mais simples que preserve auditabilidade.
- Não introduzir routing complexo, multi-wiki físico ou abstrações novas sem necessidade substantiva.
- Manter fronteiras claras entre namespaces.
- Evitar schemas globais gigantes; preferir meta-schema mínimo + variações locais por namespace.

## Persistência de estado
No fim de qualquer sessão material:
1. Atualizar os ficheiros afetados.
2. Se foi tomada uma decisão, criar ou atualizar o ADR correspondente.
3. Se surgiram dúvidas novas, atualizar `02-open-questions.md`.
4. Se houve mudança de navegação ou estrutura, atualizar `index.md`.
5. Se houve alteração de governação, atualizar o ficheiro de governance relevante.
6. Se a mudança alterar o modelo do sistema, atualizar o ficheiro-base correspondente.
7. Atualizar `roadmap/ide-roadmap.md` com o estado corrente, o que mudou, o que ficou em aberto, o próximo passo e quaisquer novas restrições.
8. Sobrescrever `handoff.md` com o checkpoint vivo mais recente.

## Hand-off obrigatório
No fim de cada sessão, produzir um resumo curto com:
- o que mudou;
- o que ficou em aberto;
- que ficheiros foram atualizados;
- qual deve ser o próximo passo;
- que ficheiro deve ser lido primeiro na próxima sessão.

Esse resumo deve ser escrito em `handoff.md`, substituindo completamente a versão anterior. `handoff.md` é sempre o estado mais recente, nunca um histórico.

## Workflow mínimo
1. Identificar fase e contexto.
2. Distinguir camadas e namespace.
3. Executar a tarefa.
4. Atualizar o estado no repo.
5. Atualizar `roadmap/ide-roadmap.md`.
6. Sobrescrever `handoff.md`.
7. Gerar handoff para a sessão seguinte.

## Roadmap, handoff e estado de sessão
- Read `index.md`, the active `roadmap/ide-roadmap.md`, and `handoff.md` at the start of every session.
- Treat `roadmap/ide-roadmap.md` as the current source of truth for implementation priorities and session state.
- Treat `handoff.md` as the latest checkpoint for the next session.
- Do not end a material session without updating the roadmap with:
  - what changed;
  - what remains open;
  - the next step;
  - any new constraints or decisions.
- Do not end a material session without overwriting `handoff.md` with the latest checkpoint.
- If the task materially changes the repository state, update the relevant artifact(s), the roadmap, and the handoff before ending the session.
- If the roadmap, handoff, and current repo state disagree, report the discrepancy before making changes.
- Do not treat `agents.md` as a session log; use it for stable rules, while session-specific progress belongs in `roadmap.md` or `progress.md` and `handoff.md`.

## GitHub Copilot / IDE Agent — regras adicionais
- Read `handoff.md` first.
- Validate with `python scripts/validate.py` before every commit and push.
- Namespaces: write only to the specific namespace matching the task domain.
- Links between namespaces must be explicit and rare.