# Instruções para o Claude Code

Este repositório é uma formação profissional em Claude Code, conduzida pela skill `ai-tutor`. Responda em português brasileiro.

- `skill_root`: `.claude/skills/ai-tutor/`, somente leitura; cópia do projeto `ai-tutor-skill`.
- `study_root`: raiz deste repositório.
- Leia `.ai-tutor/study-config.json`, `.ai-tutor/state.json` e `curriculum.md` antes de conduzir o estudo.
- Ao retomar, siga `references/workflows/session.md` da skill e priorize a sessão ativa ou interrompida retomável (`session_001` nesta revisão). Não reabra sessões concluídas; a revisão curricular não é uma sessão de aprendizagem.
- Siga os contratos de estado e aprendizagem da skill. Não invente evidências nem marque domínio por gerar código.
- `curriculum_tracks` na configuração define os IDs obrigatórios, opcionais e históricos. Ensine o núcleo de Claude Code; tópicos opcionais ou históricos só por pedido do aluno. Não apague IDs antigos.
- Use `docs/laboratorios/README.md` para selecionar prática conforme os pré-requisitos. Enunciados e dados fornecidos não são evidências.
- Em exercícios de programação, peça decisões e verificação ao aluno. Registre comandos, resultados, arquivos e a transferência para outra tarefa.
- Use dados fictícios em `projects/dados/` como ponto de partida. Não exponha dados internos em portfólio.
- Valide mudanças no estado, a partir de `skill_root`: `python3 -m scripts.validate_study <caminho absoluto da raiz do repo>`. O comando direto `python scripts/validate_study.py` falha no import nesta versão.
