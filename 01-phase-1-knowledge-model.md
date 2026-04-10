---
title: Phase 1 — Final Knowledge Model
status: research
confidence: medium
updated: 2026-04-10
provenance: ["00-space-manual.md", "00-project-origin.md"]
---

# Phase 1 — Final Knowledge Model

## Status
Active

## Goal
Definir o papel da wiki no sistema final e a sua relação com research, retrieval, notebooks, namespaces, agentes e decisões. Esta fase existe para evitar desenhar a arquitetura do repositório com pressupostos errados.

## Core thesis
A hipótese de trabalho atual é que o sistema final deve assentar num repositório único com namespaces fortes por domínio, em que a wiki funciona como camada curada de decisão, síntese e memória operacional, complementando research notebooks e retrieval em vez de os substituir.

## Questions this phase must answer

### 1. Role of the wiki
- A wiki é memória canónica, camada interpretativa, índice mestre, ou combinação destas funções?
- O que deve entrar na wiki?
- O que nunca deve entrar na wiki?

### 2. Relation with research
- O que fica em NotebookLM ou noutra camada de research?
- Quando é que research sobe a conhecimento consolidado?
- Como distinguir exploration from decision?

### 3. Relation with retrieval/corpus
- Quando é que a wiki basta?
- Quando é preciso consultar corpus amplo ou retrieval externo?
- Qual é a fronteira entre curated memory e broad coverage?

### 4. Topology and namespaces
- Que namespaces devem existir no arranque?
- Como se definem as fronteiras entre `engineering`, `systems-ai`, `personal`, `shared` e outros?
- Que tipo de relações entre namespaces devem ser permitidas?
- Quando é que um namespace deve ser extraído para uma wiki física separada?

### 5. Agent interaction
- Como deve um agente saber que namespaces existem?
- Como escolhe o namespace certo para ler ou escrever?
- Em que circunstâncias pode consultar mais de um namespace?
- Onde escreve o resultado?

### 6. Auditability and governance
- Como garantir que decisões, dúvidas, promotion e provenance são explícitas?
- Como evitar um sistema opaco de grafo/tags sem semântica clara?
- Que metadados mínimos devem ser comuns a todos os namespaces?
- Que schemas locais podem variar por domínio?

## Deliverables
- `architecture/wiki-vs-research-vs-retrieval.md`
- `architecture/namespaces-and-boundaries.md`
- `decisions/ADR-001-role-of-wiki.md`
- `decisions/ADR-002-single-repo-with-namespaces.md`
- `governance/research-to-decision.md`
- `governance/metadata-and-frontmatter.md`
- `open-questions` atualizado

## Working method
1. Formular perguntas-mãe.
2. Fazer research focada por pergunta.
3. Comparar opções e trade-offs.
4. Registar inclinações provisórias.
5. Fechar ADRs quando houver decisão suficiente.
6. Só então passar ao desenho mais detalhado do repositório e do workflow.

## Exit criteria
A Fase 1 só termina quando houver respostas suficientemente claras para:
- o papel da wiki;
- a relação wiki vs research vs retrieval;
- a topologia inicial do repositório;
- os namespaces de arranque e a sua lógica de fronteiras;
- a regra de promoção de research para conhecimento consolidado;
- o modelo mínimo de metadados e governação.

## Explicit warning
Não desenhar já stack final, frontend final, semantic router, multi-wiki físico ou plataforma final antes de fechar esta fase.
