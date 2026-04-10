---
title: "ADR-003: Topologia 7 Namespaces — Opção B Consolidada"
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-001-single-repo-with-namespaces.md", "handoff.md", "02-open-questions.md"]
tipo-meta: governance
revisao: 2026-Q4
---

# ADR-003: Topologia 7 Namespaces — Opção B Consolidada

## Status
Accepted.

## Contexto
Phase 1 estabilizou o repositório com 4 namespaces (`engineering/`, `systems-ai/`, `personal/`, `shared/`) e validação a 0 erros. A topologia inicial cobria o domínio profissional (engenharia + sistemas) mas não endereçava os domínios de vida pessoal — finançcas, família, relações, saúde, desenvolvimento pessoal — que constituem parte substantiva do uso real esperado.

Q-002 (topologia) estava decidida como single-repo com namespaces fortes (ADR-001), mas os namespaces concretos eram provisórios. Phase 2 resolve a granularidade dos namespaces sem alterar o princípio arquitectural.

## Decisão
Refatorar a topologia para **7 namespaces operacionais** mais `meta/` e `shared/`:

```
├── work/          # engineering/ + systems-ai/ (domínio profissional)
├── patrimonio/    # finançcas, imóveis, investimentos, fiscal
├── familia/       # co-parentalidade, Siena, acordos
├── relacoes/      # relações íntimas, amizades, profissionais relevantes
├── saude/         # saúde física, mental, rotinas
├── dev-pessoal/   # autoconhecimento, padrões, reflexão
└── meta/          # governance/ + decisions/ + foundations/
```

Cada namespace tem:
1. `index.md` — índice e fronteira semântica.
2. `RULES.md` — schema local mínimo com 1–3 tags específicas.

## Movimentos de conteúdo
| Antes | Depois | Motivo |
|---|---|---|
| `engineering/` | `work/engineering/` | Consolidação domínio profissional |
| `systems-ai/` | `work/systems-ai/` | Consolidação domínio profissional |
| `governance/` | `meta/governance/` | Consolidação governance |
| `decisions/` | `meta/decisions/` | Consolidação governance |
| `foundations/` | `meta/foundations/` | Material conceptual do sistema |
| `personal/` | removido | Sem conteúdo a migrar; substituído por namespaces específicos |

## Alternativas Consideradas

### Opção A — Manter topologia actual
Manter `engineering/`, `systems-ai/`, `personal/`, `shared/`. Adicionar RULES.md por namespace existente.
- _Pro_: zero movimentos, zero risco de links partidos.
- _Contra_: `personal/` é vago e não endereça os domínios de vida reais; crescimento futuro sem orientação clara.

### Opção B — 7 namespaces consolidados (escolhida)
Redefinir namespaces por domínios de vida reais.
- _Pro_: cobertura total do espaço de vida; schemas locais por domínio; privacidade diferenciada por namespace.
- _Contra_: refatoração com movimentos de ficheiros; links internos a actualizar.

### Opção C — Repo separado para domínios pessoais
Multi-repo: repo público para `work/meta/`, repo privado para vida pessoal.
- _Pro_: separação física de privacidade.
- _Contra_: over-engineering prematuro; critérios de extração do ADR-001 não atingidos.

## Trade-offs
| Dimensão | Opção A | Opção B | Opção C |
|---|---|---|---|
| Risco de migração | Nenhum | Baixo | Alto |
| Cobertura de vida | Parcial | Completa | Completa |
| Privacidade | Namespace único | Por namespace | Repo físico |
| Complexidade | Baixa | Baixa-médida | Alta |

## Justificação
A Opção B mantém o princípio do ADR-001 (single-repo, namespaces fortes) e resolve a ausência de domínios de vida reais sem introduzir complexidade nova. O custo de migração é pontual e reversível.

## Schemas locais criados
| Namespace | Tags |
|---|---|
| `work/` | `area` (jsj/carreira/competencia/ferramenta), `prioridade` (alta/media/baixa) |
| `patrimonio/` | `classe` (rendimento/imovel/fiscal/investimento), `horizonte` (curto/longo) |
| `familia/` | `quem` (siena/co-parent), `sensibilidade` (probatorio/normal) |
| `relacoes/` | `pessoa` (texto livre), `tipo-rel` (intima/amizade/profissional) |
| `saude/` | `eixo` (fisico/mental/rotina) |
| `dev-pessoal/` | `padrao` (snake_case), `fonte` (terapia/reflexao/incidente) |
| `meta/` | `tipo-meta` (governance/llm-context/cross-link), `revisao` (YYYY-QN) |

## Consequências
- Actualizar `shared/registry.md` com nova lista de namespaces.
- Actualizar `index.md` raiz com nova tabela de namespaces.
- Q-002 mantém-se `decided` (princípio não mudou, apenas granularidade).
- Q-006 mantém-se `decided` (schemas locais tornam semântica ainda mais explícita).
- `02-open-questions.md` actualizado com nota sobre refinamento de topologia.
