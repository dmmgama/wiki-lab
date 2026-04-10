---
title: "ADR-002: Papel Canónico da Wiki"
status: decision
confidence: high
updated: 2026-04-10
provenance: ["00-space-manual.md", "01-phase-1-knowledge-model.md", "02-open-questions.md"]
closes: ["Q-001"]
---

# ADR-002: Papel Canónico da Wiki

## Contexto
Q-001 estava em aberto desde o início do projecto: o que é a wiki canonicamente, o que entra, o que não entra, e como se relaciona com outros namespaces e ferramentas.

## Decisão
A wiki é a camada de síntese curada e memória operacional persistente do sistema.

## O que entra
- Decisões com racional (ADRs)
- Processos com história e fases (ex: autoconhecimento, perfilagem de pessoas, evolução de projectos)
- Conhecimento consolidado por domínio que não vale a pena redescobrir
- Cross-links intencionais entre namespaces

## O que não entra
- Raw de conversas com LLMs
- Documentos primários (normas, PDFs — ficam no NotebookLM)
- Notas temporárias sem conclusão
- Qualquer conteúdo sem frontmatter YAML completo (sem provenance não entra)

## Organização
- Namespaces com schemas de tags locais e independentes, definidos em cada RULES.md
- Sem schema global de tags
- shared/registry.md é o mapa de namespaces — não de conteúdo

## Cross-links
Permitidos e encorajados entre namespaces. Sempre explícitos como hiperlinks visíveis no Markdown. Nunca automáticos ou inferidos por embedding.

O utilizador controla quais namespaces expõe em cada sessão de LLM. Uma sessão pode receber múltiplos namespaces em simultâneo para raciocínio cross-domínio (ex: verificar simbiose entre dois projectos, ou avaliar carga pessoal face a prioridades de engenharia).

## Consequências
- Q-001 fechada como decided
- Schemas locais por namespace a definir em Phase 2 (um RULES.md por namespace)
- NotebookLM mantém-se como camada de research — não entra na wiki directamente
- Q-005 (papel do NotebookLM) permanece open mas subordinada a esta decisão

## Alternativas consideradas
- Wiki como índice puro (rejeitada — fraca para contexto de LLM)
- Wiki como tudo-em-um corpus (rejeitada — colapsa em caixa negra)
- Multi-wiki separada por domínio (rejeitada em ADR-001 — routing desnecessário; namespaces resolvem)
