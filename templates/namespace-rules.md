---
title: Template — RULES.md de Namespace
status: decision
confidence: high
updated: 2026-04-10
provenance: ["ADR-003-topology-7namespaces.md", "RULES.md"]
---

# Template — RULES.md de Namespace

> **Como usar:** Copiar este ficheiro para `[namespace]/RULES.md`. Preencher as secções com o schema local do namespace. Remover exemplos não aplicáveis.

---

```markdown
---
title: [Namespace] — Schema Local (RULES)
status: decision
confidence: high
updated: YYYY-MM-DD
provenance: ["ADR-003-topology-7namespaces.md"]
---

# RULES — [namespace]/

## Tags obrigatórias neste namespace

### `[tag-1]`
[Descrição da tag.]

| Valor | Âmbito |
|---|---|
| `valor-a` | Descrição do valor A |
| `valor-b` | Descrição do valor B |

### `[tag-2]`
[Descrição da tag. Se for texto livre, indicar exemplos e convenção de formato.]

## Campos frontmatter adicionais permitidos
- `campo-opcional`: [descrição e tipo] (ex: `"exemplo"`).

## Nota de privacidade
[Indicar se o namespace é privado, nunca exposto publicamente, ou condicionalmente exposto.]

## Exemplo de frontmatter completo
\```yaml
---
title: [Título de exemplo]
status: [research | hypothesis | decision | dropped | implemented]
confidence: [low | medium | high]
updated: YYYY-MM-DD
provenance: ["[namespace]/"]
[tag-1]: [valor]
[tag-2]: [valor]
---
\```

## Cross-links
[Descrever se e como fazer cross-links com outros namespaces. Ex: "Links para work/ permitidos quando relevante."]
```

---

## Instruções de preenchimento

1. **Identificar as 1–3 tags mais úteis** para o namespace — não mais.
2. **Definir enums fechados** quando os valores são conhecidos e estáveis.
3. **Usar texto livre** (snake_case) quando os valores são abertos (ex: `padrao`, `pessoa`).
4. **Não duplicar** campos do schema universal (`title`, `status`, `confidence`, `updated`, `provenance`).
5. **Manter o RULES.md curto** — referência operacional, não especificação exaustiva.
