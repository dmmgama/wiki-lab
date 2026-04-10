#!/usr/bin/env python3
"""
Wiki-Lab — Validação leve de frontmatter, naming e links internos.
Stdlib only. Corre na raiz do repo: python scripts/validate.py
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Pastas a ignorar na validação de frontmatter
SKIP_DIRS = {"templates", "prompts", "scripts", ".git"}

# Ficheiros raiz convencionais a ignorar (Git/GitHub standard)
SKIP_FILES = {"README.md", "AGENTS.md", "LICENSE", "LICENSE.md"}

# Campos obrigatórios (per governance/metadata-and-frontmatter.md)
REQUIRED_FIELDS = {"title", "status", "confidence", "updated", "provenance"}

# Enums válidos
VALID_STATUS = {"research", "hypothesis", "decision", "dropped", "implemented"}
VALID_CONFIDENCE = {"low", "medium", "high"}

# Pattern para frontmatter YAML
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)

# Pattern para links internos Markdown: [text](path)
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

# Pattern para naming: lowercase, hyphens, digits, underscores, dots
# Aceita prefixo underscore (_index.md) e maiúsculas em prefixo ADR (ADR-001-*.md)
VALID_NAME_RE = re.compile(r"^(_?[a-z0-9][a-z0-9._-]*\.md|ADR-\d{3}[a-z0-9-]*\.md)$")


def parse_frontmatter(text: str) -> dict | None:
    """Extrai campos do frontmatter YAML de forma simples (sem dep yaml)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            fields[key.strip()] = val.strip().strip('"').strip("'")
    return fields


def check_frontmatter(path: Path, text: str, errors: list, warnings: list):
    """Verifica presença e conteúdo do frontmatter."""
    fields = parse_frontmatter(text)
    if fields is None:
        errors.append(f"{path}: YAML frontmatter ausente (delimitadores --- não encontrados)")
        return

    for field in REQUIRED_FIELDS:
        if field not in fields:
            errors.append(f"{path}: campo obrigatório em falta: '{field}'")

    status = fields.get("status", "").lower()
    if status and status not in VALID_STATUS:
        errors.append(f"{path}: status inválido: '{status}' (válidos: {VALID_STATUS})")

    confidence = fields.get("confidence", "").lower()
    if confidence and confidence not in VALID_CONFIDENCE:
        errors.append(f"{path}: confidence inválido: '{confidence}' (válidos: {VALID_CONFIDENCE})")

    updated = fields.get("updated", "")
    if updated and not re.match(r"^\d{4}-\d{2}-\d{2}$", updated):
        warnings.append(f"{path}: 'updated' não é ISO date: '{updated}'")


def check_naming(path: Path, warnings: list):
    """Verifica convenção de nomes: lowercase, hyphens."""
    name = path.name
    if not VALID_NAME_RE.match(name):
        warnings.append(f"{path}: nome não segue convenção (lowercase, hyphens): '{name}'")


def check_links(path: Path, text: str, warnings: list):
    """Verifica links internos — path relativo deve existir."""
    for match in LINK_RE.finditer(text):
        target = match.group(2)
        # Ignorar URLs externas e âncoras
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        # Resolver path relativo ao ficheiro
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            warnings.append(f"{path}: link partido → '{target}'")


def should_skip(path: Path) -> bool:
    """Verifica se o ficheiro está numa pasta ou é um ficheiro a ignorar."""
    if path.name in SKIP_FILES:
        return True
    parts = path.relative_to(REPO_ROOT).parts
    return any(part in SKIP_DIRS for part in parts)


def main():
    errors = []
    warnings = []

    md_files = sorted(REPO_ROOT.rglob("*.md"))

    if not md_files:
        print("Nenhum ficheiro .md encontrado.")
        return 0

    for path in md_files:
        if should_skip(path):
            continue

        text = path.read_text(encoding="utf-8", errors="replace")

        check_frontmatter(path, text, errors, warnings)
        check_naming(path, warnings)
        check_links(path, text, warnings)

    # Report
    print(f"\n{'='*60}")
    print(f"Wiki-Lab Validation Report")
    print(f"{'='*60}")
    print(f"Ficheiros analisados: {len([p for p in md_files if not should_skip(p)])}")
    print(f"Erros: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print(f"\n--- ERROS ---")
        for e in errors:
            print(f"  ✗ {e}")

    if warnings:
        print(f"\n--- WARNINGS ---")
        for w in warnings:
            print(f"  ⚠ {w}")

    if not errors and not warnings:
        print("\n  ✓ Tudo válido.")

    print()
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
