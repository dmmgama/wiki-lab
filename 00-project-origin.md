---
title: Project Origin
status: decision
confidence: high
updated: 2026-04-10
provenance: ["00-space-manual.md"]
---

# Project Origin

## Status
Active

## Objective
Criar um sistema sério de gestão de conhecimento baseado num repositório único com namespaces por domínio, research notebooks, retrieval e acesso por vários LLMs, com capacidade de escalar, evitar caixa-preta semântica e manter governação explícita.

## Why this project exists
A motivação deste projeto nasce de uma limitação clara dos workflows correntes com LLMs: demasiado conhecimento relevante fica preso a chats efémeros, sessões caras, contexto implícito ou memória pouco auditável. O objetivo não é apenas “ter notas melhores”, mas construir um sistema em que conhecimento, decisões, dúvidas, research e arquitetura tenham papéis distintos, legíveis e controlados.

## Current architectural position
A posição atual do projeto é abandonar, para já, a ideia de múltiplas wikis físicas. Em vez disso, o sistema deve começar como um repositório único, versionado e acessível por vários LLMs, organizado em namespaces fortes por domínio.

Isto permite manter separação semântica, schemas locais, regras de governação específicas e legibilidade operacional, sem introduzir desde o início os custos de routing, sincronização e manutenção de uma arquitetura multi-wiki.

## Initial target model
A direção atual aponta para uma arquitetura em que:

- a wiki funciona como camada curada de decisão, síntese e memória operacional;
- ferramentas como NotebookLM servem para research, exploração e comparação de fontes;
- retrieval/corpus amplo serve para cobertura, frescura e amplitude;
- o repositório único contém namespaces por domínio, em vez de uma wiki amorfa sem fronteiras;
- relações entre domínios são explícitas, raras quando necessário, e não impostas por um schema global excessivo.

## Current constraints
- O projeto está ainda em fase de descoberta.
- O utilizador não quer depender estruturalmente de Claude devido a custo e limites de sessão.
- O cockpit de trabalho provável é VS Code + Git + GitHub Copilot, com Gemini/Google Pro como ferramenta forte de research.
- NotebookLM via MCP é um candidato forte para camada de research assistida.
- O sistema tem de ser auditável, portátil e compreensível por humanos sem depender de middleware opaco.

## Current leanings
- A wiki não deve substituir o research corpus nem a knowledge base ampla.
- O sistema deve começar com um repositório único organizado por namespaces fortes.
- Multi-wiki físico fica adiado até existir pressão real de escala, privacidade, equipa ou ciclo de vida distinto.
- É necessário evitar grafos e tags opacos sem semântica governada.
- O `wiki-lab` existe como fase e modo de trabalho, não como plataforma paralela complexa.

## Non-goals for now
- Não implementar já uma plataforma final online.
- Não decidir já storage final, grafo final, autenticação ou frontend final.
- Não introduzir já routing semântico pesado, orchestration frameworks ou multi-agent stacks complexas.
- Não fundir todos os domínios num schema global único.
- Não assumir que o modelo inicial de arquitetura está correto em todos os detalhes.

## What this project needs to answer
1. Qual é o papel canónico da wiki no sistema final?
2. Como se articula a wiki com research notebooks, retrieval e memória operacional?
3. Que namespaces devem existir no arranque e com que fronteiras?
4. Como evitar que o sistema se torne uma caixa preta semântica?
5. Como permitir acesso consistente por vários LLMs?
6. Que arquitetura mínima do repositório e da governação permite descobrir a forma final do sistema?

## Immediate next step
Fechar a Fase 1: definir o modelo final de conhecimento, a lógica de namespaces e a governação mínima antes de expandir a implementação.
