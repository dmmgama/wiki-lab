---
title: Namespaces e Fronteiras Semânticas
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-001", "Q-002", "Q-004"]
---

# Namespaces e Fronteiras Semânticas

## Status
Active. Resolve Q-002 (topologia), Q-004 (navegação agentes). Atualiza 02-open-questions.md.

## Namespaces Iniciais
1. `/engineering` - Estrutural (reabilitação sísmica, betão pré-esforçado, Eurocódigos, stack SAP2000/ETABS).[file:7]
2. `/systems-ai` - Knowledge mgmt (wiki, agents, retrieval).[file:2]
3. `/personal` - Carreira/financeiro (prudente).[file:5]
4. `/shared` - Governance/ADR comuns (rádio).[file:1]

P1: Namespaces baseados no teu perfil actual; expande só com uso real.[file:7]
P2: Registry central em `/shared/registry.md` lista namespaces, regras de escrita.[file:2]

## Separação e Fronteiras Semânticas
- Separação física: Pastas Git raiz (`/engineering/`, etc.), schemas frontmatter locais (domínio-specific), metadados globais mínimos (provenance, status).[file:2]
- Fronteiras:
  | Namespace     | Fronteira Semântica Principal                  | Exemplos Conteúdo Curado                  |
  |---------------|------------------------------------------------|-------------------------------------------|
  | engineering  | Decisões técnicas estruturais, Eurocódigos    | ADRs betão, snteses sísmica [file:1]     |
  | systems-ai   | Arquitetura wiki/agents/retrieval             | Políticas promotion, workflows [file:5]   |
  | personal     | Carreira/prudente financeiro                  | Planos OE, finanças [file:7]              |
  | shared       | Decisões transversais, índices                | ADRs globais, registry [file:2]           |

Evita bleed: Agentes escrevem só no namespace matching query domínios; erro se ambiguo.[file:4]

## Cross-Links Permitidos
- Explícitos e raros: Markdown links bidirecionais (`[ver /systems-ai/agents.md]`), sem tags/edges automáticos.[file:1]
- Permitido: Referências factuais (ex: ADR em shared linka engineering), índices em shared.
- Proibido: Links densos (>5 por ficheiro), routing semântico implícito.
Trade-off: Auditável (Git diff), mas manual; escala com revisão.[file:2]

## Critérios Extração
- Permanece no namespace: Contedo curado estável, <10% cross-links, ciclo vida alinhado repo único.[file:2]
- Extrai para artefacto separado (multi-repo/wiki física): 
  1. Pressão real (equipa>1, privacidade, escala>100 ficheiros/namespace).
  2. Ciclo vida distinto (ex: personal privado).
  3. Manutenção diverge (sync custoso).
Monitoriza via métricas Git (tamanho, commits cross).[file:5]
Posição: Adia extração; single-repo domina (baixa complexidade).[file:2]

## Evita Caixa-Preta Semântica
- Relações explícitas (links/índices) > semântica implícita (grafos/tags).[file:1]
- Registry simples guia agentes (sem router pesado).[file:4]
- Provenance obrigatória: Todo ficheiro linka origem (research/ADR).[file:2]
Resultado: Legível humano/LLM, zero opacidade, manutenção Git nativa.[file:6]