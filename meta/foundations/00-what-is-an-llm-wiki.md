---
title: O que é uma LLM Wiki
status: research
confidence: medium
updated: 2026-04-10
provenance: ["Q-001", "00-project-origin.md"]
---

# O que é uma LLM Wiki

## Definição no Projeto
Uma LLM wiki é a camada curada de decisão, síntese e memória operacional num repositório único com namespaces por domínio. Serve como source of truth legível por humanos e LLMs, complementando research notebooks (exploração volátil) e retrieval (cobertura ampla e fresca) [file:2][file:4].

## Distinções Chave
- **Research**: Exploração inicial, comparação de fontes, hipóteses não validadas; fica em notebooks (ex: NotebookLM); volátil, não promovido sem consolidação.
- **Curated wiki**: Conteúdo estabilizado (definições canónicas, ADRs, sínteses); entra via promoção explícita; auditável e versionado.
- **Retrieval**: Acesso a corpus externo/amplo para frescura; wiki não substitui, indexa ou referencia.
- **Implementação**: Artefatos operacionais (scripts, schemas); wiki documenta decisões, não executa [file:1][file:3].

## Papel dos Namespaces
Namespaces fortes por domínio (ex: engineering, systems-ai) impõem fronteiras semânticas, schemas locais e regras de governance específicas. Relações entre namespaces são explícitas e raras; sem routing semântico pesado no arranque. Permite escalabilidade sem multi-wiki físico [file:2][file:4].

## Conteúdo: Entra/Não Entra
- **Entra**: Decisões fechadas (ADRs), sínteses curadas, políticas de governance, índices de namespaces, metadados mínimos (provenance, status).
- **Não entra**: Notas exploratórias, dumps de chats, fontes raw não sintetizadas, hipóteses em aberto (para 02-open-questions.md), implementação volátil [file:1][file:3].

## Auditabilidade, Provenance e ADRs
Wiki garante auditabilidade via provenance explícita (links a research/ADRs), versionamento Git e schemas frontmatter comuns (status, data, autor). ADRs registam trade-offs e racional; promoção requer revisão. Evita black-box: sem tags opacos, grafos globais ou semântica implícita [file:1][file:2].