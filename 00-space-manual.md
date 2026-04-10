---
title: Wiki Lab — Space Manual
status: decision
confidence: high
updated: 2026-04-10
provenance: ["00-project-origin.md"]
---

# Wiki Lab — Space Manual

## Status
Active

## Purpose
Este Space existe para desenhar, criticar e evoluir um sistema sério de knowledge management baseado num repositório único com namespaces por domínio, research notebooks, retrieval e acesso por vários LLMs.

O Space não é a plataforma final. É o ambiente de trabalho para definir a plataforma final com rigor, sem misturar pesquisa, hipótese, decisão e implementação.

## What this Space is
- Um laboratório de arquitetura.
- Um lugar para research orientado a decisão.
- Um repositório de contexto persistente do projeto.
- Um meio para auditar o raciocínio do utilizador e a evolução do plano.
- Um espaço para separar research, wiki curada, decisões, dúvidas e roadmap.

## What this Space is not
- Não é a wiki final em operação.
- Não é um dump de chats.
- Não é um substituto para Git ou para o repositório do projeto.
- Não é o local onde ficam decisões implícitas sem registo.
- Não é um grafo opaco de tags sem semântica clara.
- Não é uma meta-plataforma separada do repositório real.

## Core operating model
O modelo de trabalho deste Space assenta em quatro camadas:

1. **Research** — exploração, comparação, levantamento de estado da arte e análise de subtemas.
2. **Curated wiki** — memória consolidada, decisões, enquadramento e síntese estável.
3. **Open questions** — incertezas explicitadas, auditáveis e ligadas a decisões futuras.
4. **Roadmap** — sequência de fases, critérios de saída e próximos passos.

Regra essencial: research não é decisão; hipótese não é arquitetura; implementação não deve antecipar semântica.

## Roadmap of the Space

### Phase 1 — Define the final knowledge model
Objetivo: perceber como a wiki final deve funcionar no ecossistema geral.

Perguntas centrais:
- qual é o papel canónico da wiki;
- o que fica em research e o que sobe para a wiki;
- qual é a topologia mínima do repositório;
- que namespaces devem existir;
- como evitar caixa preta semântica;
- como deve funcionar o routing entre namespaces e agentes.

### Phase 2 — Design the repository and workflow
Objetivo: desenhar o repositório operativo e o workflow de curadoria, research e decisão.

Perguntas centrais:
- qual a estrutura mínima do repo;
- como integrar NotebookLM e outros agentes;
- como guardar dúvidas, hipóteses e ADRs;
- como garantir auditabilidade;
- como definir schemas globais mínimos e schemas locais por namespace.

### Phase 3 — Define the implementation roadmap
Objetivo: transformar a visão e a arquitetura do repositório num plano de execução sério.

Perguntas centrais:
- que MVP construir;
- que backlog adiar;
- que arquitetura técnica implementar primeiro;
- que critérios definem passagem de laboratório para sistema operacional.

## Files in this Space

### Current core files
- `00-space-manual.md` — este documento.
- `00-project-origin.md` — origem, objetivo, direção inicial e restrições.
- `01-phase-1-knowledge-model.md` — perguntas, método e critérios da Fase 1.
- `02-open-questions.md` — dúvidas, tensões e hipóteses em aberto.

### Expected future files
- `foundations/*` — compreensão do modelo LLM Wiki e dos seus limites.
- `architecture/*` — opções e desenho do sistema.
- `decisions/*` — ADRs e decisões fechadas.
- `governance/*` — políticas de promotion, naming, routing, metadata e revisão.
- `roadmap/*` — plano final por fases.

## How to use this Space
1. Ler primeiro o manual e os ficheiros-base antes de responder a perguntas estratégicas.
2. Tratar `00-project-origin.md` como origem do problema.
3. Tratar `01-phase-1-knowledge-model.md` como plano de decisão vigente.
4. Tratar `02-open-questions.md` como backlog de incerteza.
5. Distinguir sempre entre research, hipótese, decisão e implementação.
6. Quando surgir decisão relevante, propor a sua formalização em ficheiro próprio.
7. Quando surgir nova dúvida estrutural, registar explicitamente em open questions.
8. Quando surgir mudança de direção, atualizar os ficheiros-base antes de continuar a expandir o contexto.

## How to update the context of the Space
Atualizar o contexto deste Space significa converter progresso em artefactos curados.

### Update rules
- Chats úteis devem ser convertidos em MDs curados.
- Novas dúvidas devem entrar em `02-open-questions.md`.
- Decisões fechadas devem sair de open questions e virar ADRs.
- Mudanças no plano devem atualizar `01-phase-1-knowledge-model.md` ou ficheiro equivalente da fase ativa.
- Mudanças de propósito, âmbito ou restrições devem atualizar `00-project-origin.md`.
- Quando uma fase muda, o roadmap do manual deve ser atualizado.
- Se a topologia do sistema mudar, isso deve ser refletido imediatamente nos ficheiros-base.

### What not to do
- Não deixar decisões materiais apenas em chats.
- Não acumular ficheiros redundantes com versões quase iguais.
- Não usar o Space como armazém indiferenciado de links e PDFs.
- Não adicionar contexto sem o classificar como research, decisão, dúvida ou orientação.
- Não reabrir hipóteses já abandonadas sem nova razão substantiva.

## Query modes to use in this Space

### Mode A — Clarify
Usar quando a pergunta é conceptual.
Saída esperada: reconstrução do problema, distinções semânticas, hipóteses, riscos.

### Mode B — Decide
Usar quando já há opções suficientes e é preciso tomar posição.
Saída esperada: opções 2–4, trade-offs, posição recomendada, implicações.

### Mode C — Plan
Usar quando já existe direção e é preciso plano por fases.
Saída esperada: roadmap, entregáveis, critérios de saída, dependências.

### Mode D — Audit
Usar quando é preciso rever consistência do Space.
Saída esperada: conflitos, lacunas, redundâncias, drift e próximos ajustes.

## Quality rules for answers in this Space
- BLUF curto no início.
- Tom técnico, assertivo e sem fluff.
- Pressupostos numerados quando relevante.
- 2–4 opções com trade-offs quando houver decisão.
- Posição clara quando o contexto permitir.
- Aviso explícito se houver overengineering.
- Ligação ao perfil concreto do utilizador.

## Criteria for a healthy Space
Este Space está saudável quando:
- o contexto principal cabe em poucos ficheiros canónicos;
- as dúvidas estão explícitas;
- as decisões estão separadas das hipóteses;
- o roadmap está alinhado com a fase real do projeto;
- a topologia assumida pelo Space está alinhada com a decisão atual do projeto;
- o utilizador consegue perceber rapidamente onde está e o que falta decidir.

## First instruction to any new thread
Antes de responder, lê o manual do Space e os ficheiros-base, reconstrói a fase atual do projeto e distingue claramente entre research, hipótese, decisão e implementação.
