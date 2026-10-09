# Proposta: formação profissional em Claude Code

## Objetivo

Formar um usuário capaz de conduzir uma entrega de software com Claude Code, desde a leitura do repositório até uma PR revisável, com testes, limites conhecidos e decisões que consiga explicar.

## Leitura da base

O projeto é um programa de estudo em arquivos, sem aplicação web ou backend. `curriculum.md` organiza a trilha; `.ai-tutor/study-config.json` registra o contrato do estudo; `.ai-tutor/state.json` mantém progresso e retomada; `session-log.md` projeta as sessões. A skill em `.claude/skills/ai-tutor/` fornece workflows e validadores Python, com biblioteca padrão e Python 3.11+.

A base anterior tinha 17 tópicos, nenhum com evidência, e uma sessão interrompida sobre o loop agêntico. Já havia fundamentos de Claude Code, mas o objetivo combinava ecossistema Claude, Python, agente via API e oferta comercial. Skills, MCP e hooks tinham profundidade básica; faltavam competências explícitas de planejamento, debugging, revisão de PR, retomada, consumo, subagentes, worktrees e CI. As pastas de lições e projetos estavam vazias.

Havia também uma inconsistência de avaliação: tópicos “básicos” com meta 60 apareciam no mesmo checklist cuja regra de conclusão exige 80. A nova trilha distingue conclusão obrigatória de familiarização opcional.

## Melhoria implementada

- Reposicionar README, currículo, instruções e configuração para Claude Code.
- Organizar 21 competências obrigatórias em sete fases, com entregas e pré-requisitos.
- Disponibilizar oito laboratórios, dados fictícios, um guia de trabalho e um modelo de entrega.
- Preservar a manutenção industrial como cenário de prática, sem exigir um cliente ou venda para concluir.
- Mover agente via API para aprofundamento opcional. Conservar Cowork e tópicos comerciais como histórico fora do núcleo.
- Manter os 17 IDs existentes, acrescentar nove e preservar integralmente a sessão, o checkpoint e o próximo foco.
- Manter prazo, marco de uso diário e orçamento existentes. A distribuição usa 100 h de trilha e 4 h de recuperação; não promete domínio em tempo fixo.
- Manter a skill vendorizada sem alterações. Adaptar a formação pelo contrato do estudo.

## Critérios de aceite

1. README, currículo, configuração e instruções descrevem o mesmo objetivo.
2. Todos os IDs de tópicos do estado pertencem a uma única trilha: obrigatória, opcional ou histórica.
3. Cada competência obrigatória tem enunciado, entrega e laboratório relacionado.
4. Não há progresso concedido pela migração; IDs, evidências e sessões anteriores são preservados.
5. O validador de estudo passa; links locais e dados de prática são verificáveis.
6. A PR descreve a mudança de escopo e as limitações da validação.

## Continuidade

As lições personalizadas continuam sendo geradas pelo tutor conforme o diagnóstico, em vez de preencher o estado com aulas não realizadas. O material estático permite começar as práticas e revisar o método. Evoluções futuras podem acrescentar exemplos em outras linguagens e atualizar a skill em uma PR dedicada.

O validador de pacote da skill já falha por ausência de `agents/openai.yaml`; o validador do estudo passa. A mudança curricular não corrige nem modifica a cópia da skill.
