---
title: Open Questions
status: research
confidence: medium
updated: 2026-04-10
provenance: ["01-phase-1-knowledge-model.md"]
---

# Open Questions

## Purpose
Este documento regista dúvidas, tensões, hipóteses e perguntas em aberto que condicionam a arquitetura do sistema. O objetivo não é guardar perguntas soltas, mas tornar a incerteza auditável e operacional.

## How to use this file
- Uma pergunta aqui não é uma decisão.
- Cada pergunta deve poder originar research, comparação, ADR ou política.
- Quando uma questão ficar resolvida, deve ser ligada à decisão correspondente.
- Quando uma questão deixar de importar, deve ser marcada como dropped, não apagada.

## Status model
- `open`
- `researching`
- `decided`
- `dropped`

---

## Q-001 — What is the canonical role of the wiki?
**Status:** researching  
**Why it matters:** sem esta resposta, todo o resto fica enviesado.  
**Current leaning:** a wiki deve ser camada curada de decisão, síntese e memória operacional, não substituto total de research ou corpus amplo.  
**What would resolve it:** comparação explícita entre wiki, notebook, retrieval e corpus. ADR formal em falta.  
**Related:** `foundations/00-what-is-an-llm-wiki.md` (cobre definição e distinções, mas sem ADR dedicado).

## Q-002 — What is the right topology: single repo with namespaces, or something else?
**Status:** decided  
**Why it matters:** esta decisão afeta governação, semântica, manutenção, legibilidade e escala.  
**Resolution:** repositório único com namespaces fortes. Critérios de extração futura definidos.  
**Decided by:** `decisions/ADR-001-single-repo-with-namespaces.md`, `governance/namespaces-and-boundaries.md`.

## Q-003 — What should live in research and never be promoted to the wiki?
**Status:** decided  
**Why it matters:** sem esta fronteira, a wiki degrada-se em dump de exploração.  
**Resolution:** política de promoção com critérios explícitos (≥3 fontes, trade-offs, confidence high, <1000 palavras). Material volátil, exploratório e não sintetizado fica fora.  
**Decided by:** `governance/research-to-decision.md`.

## Q-004 — How should agents navigate namespaces and decide where to read or write?
**Status:** decided  
**Why it matters:** é central para o objetivo multi-LLM sem cair em routing excessivo.  
**Resolution:** registry simples em `shared/registry.md` com lista de namespaces, fronteiras e regras de escrita. Agentes consultam registry no arranque per `agents.md`.  
**Decided by:** `shared/registry.md`, `agents.md`.

## Q-005 — What is the right role of NotebookLM in the system?
**Status:** open  
**Why it matters:** existe risco de usar NotebookLM como research layer útil ou de o transformar indevidamente em memória principal.  
**Current leaning:** NotebookLM deve servir para research e exploração, não como source of truth final.  
**What would resolve it:** definir claramente research workflow e output esperado dessa camada.

## Q-006 — How to avoid semantic black-box behavior?
**Status:** decided  
**Why it matters:** o utilizador quer evitar um sistema onde o grafo, tags e relações deixam de ser inteligíveis.  
**Resolution:** relações explícitas via links/índices, provenance obrigatória, meta-schema mínimo com campos validáveis, sem grafos/tags opacos.  
**Decided by:** `governance/metadata-and-frontmatter.md`, `governance/namespaces-and-boundaries.md` (secção "Evita Caixa-Preta Semântica").

## Q-007 — What exactly is wiki-lab now?
**Status:** researching  
**Why it matters:** o `wiki-lab` pode continuar útil como fase de descoberta, mas não deve tornar-se meta-sistema regressivo.  
**Current leaning:** `wiki-lab` deve ser fase, Space e modo de trabalho; o artefacto físico deve ser o próprio repositório evolutivo.  
**What would resolve it:** definição clara do âmbito, outputs e critérios de transição para execução mais madura.

## Q-008 — What is the minimum viable stack for exploration?
**Status:** open  
**Why it matters:** há risco de escolher uma stack final cedo demais.  
**Current leaning:** VS Code + Git + Copilot + Gemini/NotebookLM é suficiente para a fase inicial.  
**What would resolve it:** distinguir tooling de exploração de infraestrutura de produto.

## Q-009 — What kind of visual model is actually useful?
**Status:** open  
**Why it matters:** o utilizador quer grafo e outros modos, mas o grafo global pode degradar rapidamente em hairball.  
**Current leaning:** subgrafos locais, topic maps e timelines parecem mais úteis do que um grafo global como vista principal.  
**What would resolve it:** critérios de utilidade por modo de visualização.

## Q-010 — What must be understood before any architectural commitment?
**Status:** open  
**Why it matters:** há necessidade explícita de compreender perfeitamente a lógica do LLM Wiki antes de decidir o sistema.  
**Current leaning:** é necessária uma secção foundations e possivelmente um agente de entendimento/auditoria separado do agente arquiteto.  
**What would resolve it:** criar e validar páginas foundations antes de ADRs estruturais fortes.
