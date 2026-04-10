# Wiki Lab

Sistema de knowledge management baseado num repositório único com namespaces por domínio, Markdown como formato canónico, governance explícita e separação clara entre research, curated wiki, decisões e implementação.

## Quick start

1. Ler [index.md](index.md) — índice de navegação raiz.
2. Ler [agents.md](agents.md) — instruções para agentes LLM.
3. Ler [roadmap/ide-roadmap.md](roadmap/ide-roadmap.md) — estado de execução.
4. Ler [handoff.md](handoff.md) — checkpoint da última sessão.

## Namespaces

| Namespace | Pasta | Descrição |
|-----------|-------|-----------|
| engineering | `engineering/` | Engenharia estrutural, Eurocódigos, SAP2000/ETABS |
| systems-ai | `systems-ai/` | Arquitectura wiki, agents, retrieval |
| personal | `personal/` | Carreira, financeiro |
| shared | `shared/` | Governance, ADRs transversais, registry |

## Validação

```bash
python scripts/validate.py
```

## Documentação

- [00-space-manual.md](00-space-manual.md) — manual do Space
- [00-project-origin.md](00-project-origin.md) — origem do projecto
- [governance/](governance/) — políticas e meta-schema
- [decisions/](decisions/) — ADRs
- [templates/](templates/) — templates para novos ficheiros
