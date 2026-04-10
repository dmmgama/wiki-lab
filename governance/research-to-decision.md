---
title: Política de Promoção Research para Decisão
status: decision
phase: 1
confidence: high
updated: 2026-04-10
provenance: ["01-phase-1", "Q-003", "agents.md"]
---

# Definições Distintas
- **Research**: Exploração volátil, notas brutas, fontes não sintetizadas, status `research`.
- **Hipótese**: Posição provisória testável, status `hypothesis`, ligada a Q-XXX.
- **Decisão**: Fechada por critérios, status `decision`, em ADR ou ficheiro curado.
- **Implementação**: Código/config em repo principal, status `implemented`.
- **Dropped**: Rejeitada explicitamente, status `dropped`, razão documentada.

# Critérios de Promoção
Research sobe para wiki curada se:
1. ≥3 fontes independentes corroboram (ou 1 ADR).
2. Trade-offs comparados (2-4 opções, tabela).
3. Critérios de resolução explícitos (per Q-XXX).
4. Confidence `high`; risco baixo para teu perfil (engenharia conservadora).
5. Sintetizado <1000 palavras; sem fluff.

Exemplo tabela trade-offs:
| Opção | Complexidade | Auditabilidade | Manutenção | Recomendado |
|-------|--------------|----------------|------------|-------------|
| A     | Baixa       | Alta          | Baixa     | Sim        |

# Quando Fica em Research
- Volátil/exploratório (e.g., estado da arte fresco).
- Hipótese não testada.
- Cobertura ampla sem síntese (usar retrieval).
- Dropped sem valor curado.

# Papel de Open Questions, ADRs e Curadoria
- **Open Questions**: Backlog em `02-open-questions.md`; status `open/researching`. Resolve via research → promoção.
- **ADRs**: Formato MADR para decisões estruturais (e.g., ADR-001 namespaces).
- **Curadoria Humana**: Tu decides promoção; agente propõe, nunca auto-promove. Revisão anual por namespace.

# Fecho de Questão
Questão fecha se:
- Critérios acima satisfeitos.
- Documentado em ADR ou ficheiro `status: decision`.
- Link em `02-open-questions.md` → `decided`.
- Sem regresso salvo nova evidência substantiva.