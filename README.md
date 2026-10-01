# Formação Claude: trabalho e primeiros serviços com IA

Programa de estudos de 3 meses (até 2026-12-31, 4 h/semana) para usar o Claude Code no trabalho diário e criar uma primeira oferta de serviço com IA como renda extra. Não inclui construir produto próprio.

O programa é conduzido com a skill [`ai-tutor`](https://github.com/14lucas-mendes/ai-tutor-skill), instalada em `.claude/skills/ai-tutor/` para funcionar também em sessões na nuvem.

## Como estudar

Abra uma sessão do Claude Code neste repositório e peça, por exemplo:

- `/ai-tutor continue meus estudos`
- `/ai-tutor /licao`: próxima lição
- `/ai-tutor /review`: revisar pontos fracos
- `/ai-tutor /progress`: ver progresso medido

## Estrutura

| Caminho | Conteúdo |
| --- | --- |
| `curriculum.md` | Fases, tópicos e critérios de conclusão |
| `session-log.md` | Registro das sessões |
| `flashcards.md` | Cartões de revisão espaçada |
| `lessons/` | Lições geradas |
| `projects/` | Entregas práticas (workflows, scripts, oferta de serviço) |
| `media/` | Materiais de apoio (não contam como evidência) |
| `.ai-tutor/` | Estado canônico em JSON (não editar à mão) |
| `.claude/skills/ai-tutor/` | Cópia da skill (origem: `ai-tutor-skill`, commit `db41bf3`) |

## Atualizar a skill

A cópia não se atualiza sozinha. Para trazer uma versão nova do repositório `ai-tutor-skill`, substitua `SKILL.md`, `LICENSE`, `references/`, `assets/` e `scripts/` em `.claude/skills/ai-tutor/` e atualize o commit de origem acima.
