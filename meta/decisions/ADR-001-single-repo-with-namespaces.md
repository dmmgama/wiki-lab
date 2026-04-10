---
title: "ADR-001: Repositório Único com Namespaces Fortes"
status: decision
confidence: high
updated: 2026-04-10
provenance: ["Q-002", "01-phase-1-knowledge-model.md"]
---

# ADR-001: Repositório Único com Namespaces Fortes

## Status
Accepted.

## Contexto
Problema: Workflows com LLMs geram conhecimento efémero, sem separação semântica; multi-wiki introduz routing/sincronização precoce, risco de black-box. Necessário sistema auditável, legível, escalável para domínio único (engenharia estrutural) com potencial multi-domínio [file:1][file:4].

## Decisão
Adotar repositório único (Git) com namespaces fortes por domínio (ex: `engineering/`, `systems-ai/`). Schemas locais, metadados globais mínimos; relações explícitas via links/índices [file:2].

## Alternativas Consideradas
1. **Multi-wiki físico**: Wikis separadas por domínio.
2. **Repo monolítico sem namespaces**: Tudo num espaço plano.
3. **Grafo semântico global**: Tags/edges automáticos.

## Trade-offs
| Opção | Complexidade | Auditabilidade | Manutenção | Adequação Perfil |
|-------|--------------|----------------|------------|------------------|
| **Single-repo + namespaces (escolhida)** | Baixa | Alta (Git + frontmatter) | Baixa (um repo) | Alta (simples, VS Code/Git) |
| Multi-wiki | Alta (routing/sync) | Média | Alta | Baixa (overeng) |
| Monolítico | Baixa | Baixa (sem fronteiras) | Média | Média |
| Grafo global | Alta | Baixa (opaco) | Alta | Baixa [file:1][file:3].

## Justificação e Adiamento de Multi-wiki
Single-repo resolve separação semântica sem custos extras; multi-wiki adiado até pressão real (escala/privacidade/equipa). Implicações:
- **Governance**: Promoção via revisão; open-questions central.
- **Schema**: Frontmatter global (provenance/status); local por namespace.
- **Workflow**: Agentes leem/escrevem via registry simples; Phase 1 foca definição [file:2][file:4].

## Consequências
Atualizar `01-phase-1-knowledge-model.md` (Q-002 resolvida); monitorizar extração futura via critérios (ex: ciclo de vida distinto).