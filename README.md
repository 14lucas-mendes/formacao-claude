# Formação Claude: Python, agentes e automação para transição de carreira

Programa de estudos de 6 meses (até 2027-03-31, 4 h/semana, com marco de uso diário em 2026-12-31) para a primeira etapa de uma transição de carreira (manutenção ferroviária → automação, agentes de IA e desenvolvimento): uso do Claude Code e do ecossistema Claude no trabalho, Python com testes, um agente simples com a API do Claude, portfólio no GitHub e uma primeira oferta de serviço. Não inclui construir produto próprio.

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
