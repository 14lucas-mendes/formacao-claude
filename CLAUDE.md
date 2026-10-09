# Instruções para o Claude Code

Este repositório é uma formação profissional em Claude Code, conduzida pela skill `ai-tutor`. Responda em português brasileiro.

- `skill_root`: `.claude/skills/ai-tutor/`, somente leitura; cópia do projeto `ai-tutor-skill`.
- `study_root`: raiz deste repositório.
- Leia `.ai-tutor/study-config.json`, `.ai-tutor/state.json` e `curriculum.md` antes de conduzir o estudo.
- Ao retomar, siga `references/workflows/session.md` da skill e priorize a sessão ativa ou interrompida retomável (`session_001` nesta revisão). Não reabra sessões concluídas; a revisão curricular não é uma sessão de aprendizagem.
- Siga os contratos de estado e aprendizagem da skill. Não invente evidências nem marque domínio por gerar código.
- `.ai-tutor/study-config.json` é a única fonte vigente de `curriculum_tracks`. Arquivos em `.ai-tutor/migrations/` são snapshots históricos; não os use para selecionar tópicos ou calcular progresso.
- Em `/progress`, reporte domínio, retenção, evidências e pendências de conclusão somente para `core_topic_ids`. Cite opcionais e históricos à parte, sem incluí-los como pendências da formação.
- Em `/review`, filtre cartões, pontos fracos e evidências por `core_topic_ids`. Em `/licao`, selecione tópicos do núcleo na ordem do currículo, respeitando pré-requisitos e a retomada da sessão. Inclua opcionais ou históricos somente por pedido explícito do aluno; preserve seus registros.
- O `status` de um tópico indica domínio, não sua trilha. Um histórico `not_started` não é uma pendência obrigatória. Não altere esses status nem apague IDs para ocultá-los.
- Use `docs/laboratorios/README.md` para selecionar prática conforme os pré-requisitos. Enunciados e dados fornecidos não são evidências.
- Em exercícios de programação, peça decisões e verificação ao aluno. Registre comandos, resultados, arquivos e a transferência para outra tarefa.
- Use dados fictícios em `projects/dados/` como ponto de partida. Não exponha dados internos em portfólio.
- Valide classificação e checklist antes de conduzir o estudo e após mudanças de currículo: `python3 scripts/validate_curriculum.py`, a partir de `study_root`. Se falhar, corrija a classificação antes de selecionar uma nova lição ou reportar progresso.
- Valide mudanças no estado, a partir de `skill_root`: `python3 -m scripts.validate_study <caminho absoluto da raiz do repo>`. O comando direto `python scripts/validate_study.py` falha no import nesta versão.
