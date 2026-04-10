# IDE Implementation Prompt — Wiki Lab

## Context
You are working inside the `Wiki-Lab` repository.

This repository is a single-repo knowledge management system with strong namespaces by domain.
The architecture has already been decided and documented in the Space and in the repo artifacts.

Read these files first and treat them as priority context:
- `agents.md`
- `foundations/00-what-is-an-llm-wiki.md`
- `governance/metadata-and-frontmatter.md`
- `governance/research-to-decision.md`
- `decisions/ADR-001-single-repo-with-namespaces.md`
- `00-space-manual.md` if present in the repo
- `00-project-origin.md` if present in the repo
- `01-phase-1-knowledge-model.md` if present in the repo
- `02-open-questions.md` if present in the repo

## Current architectural decisions
- Single repository.
- Strong namespaces by domain.
- Multi-wiki physical split is deferred.
- Markdown is the canonical storage format.
- Governance and provenance are explicit.
- Research, curated wiki, decisions, and implementation are distinct layers.
- Avoid semantic black boxes.
- Avoid premature routing complexity.
- Keep the system simple and auditable.

## Your task
Implement the next practical layer of the repo, not the architecture debate.

### Immediate goals
1. Create or normalize the repository scaffold so it matches the agreed namespace model.
2. Create minimal index/navigation files at the repo root and inside each namespace.
3. Create or normalize templates for:
   - research notes
   - wiki pages
   - ADRs
   - open questions
4. Add a lightweight validation workflow for:
   - YAML frontmatter presence
   - required metadata fields
   - file naming conventions
   - basic internal link sanity
5. Ensure the repo is easy to navigate for both humans and LLM agents.

## Constraints
- Do not redesign the architecture.
- Do not introduce multi-wiki physical separation.
- Do not add graph-database or semantic-router complexity.
- Do not overengineer.
- Prefer small, inspectable Markdown-first solutions.
- If you need to make a choice, choose the simplest option that preserves auditability.

## Expected output
- A clear folder structure.
- Minimal working templates.
- A root index/navigation file.
- Any small scripts needed for validation.
- A short report listing what was created and what remains open.

## Working method
1. Inspect the current repository structure.
2. Compare it against the agreed model.
3. Propose the smallest corrective implementation.
4. Make the changes.
5. Summarize the changes and any unresolved questions.

## If something is inconsistent
If the existing repo conflicts with the agreed model, stop and report the inconsistency before making large changes.