# Laboratórios da formação

Estes são enunciados de prática, não soluções nem lições já realizadas. O tutor seleciona o exercício conforme os pré-requisitos e registra a tentativa avaliada. Use o [modelo de entrega](../templates/entrega.md) e o [guia profissional](../guia-profissional.md).

## Sequência

| Laboratório | Fase | Tempo de prática dentro da fase | Resultado |
| --- | --- | --- | --- |
| [01 — Ambiente](01-ambiente.md) | 1 | 3–4 h | Instalação, primeira tarefa e recuperação |
| [02 — Contexto e plano](02-contexto-e-plano.md) | 2 | 4–6 h | Instruções, plano e retomada |
| [03 — Desenvolvimento e PR](03-desenvolvimento-e-pr.md) | 3 | 8–10 h | Feature, bug corrigido e PR revisada |
| [04 — Automação e custos](04-automacao-e-custos.md) | 4 | 6–8 h | CLI mantida e medição |
| [05 — Extensões](05-extensoes.md) | 5 | 5–6 h | Skill, MCP e hook testados |
| [06 — Subagentes e worktrees](06-subagentes-e-worktrees.md) | 5 | 4–6 h | Trabalho isolado e integração |
| [07 — CLI e CI](07-cli-e-ci.md) | 6 | 6–8 h | Análise programática e pipeline |
| [08 — Projeto integrador](08-projeto-integrador.md) | 7 | 5–6 h | Demonstração e avaliação de transferência |

Essas horas já fazem parte das 104 h. O tempo restante cobre explicações, tentativas, revisão espaçada e registro. Refaça exercícios quando a evidência não demonstrar autonomia.

## Preparação comum

Use um repositório de prática seu para os exercícios de software, mantendo esta formação como registro. Crie `projects/<slug>/entrega.md` aqui com os links ou caminhos da prática. Não altere o pacote `.claude/skills/ai-tutor/` nos exercícios de extensões.

Python 3.11+ e a biblioteca padrão bastam para começar. Use `unittest` se ainda não tiver um test runner. Uma ferramenta extra só entra quando seu benefício é explicado. Instalação, MCP e CI dependem do acesso do aluno; uma limitação deve ser registrada, sem inventar execução.

Os [dados fictícios](../../projects/dados/README.md) permitem começar sem dados internos. No código de prática, crie arquivos de teste pequenos e determinísticos; nunca dependa de uma resposta do modelo para calcular o esperado.

## Avaliação

Em cada laboratório, entregue arquivos ou links, comandos e resultados; explique uma decisão; e faça a transferência sem receber a solução. O tutor avalia cada tópico separadamente segundo o contrato da skill. Um laboratório entregue não conclui automaticamente todos os tópicos relacionados.

Se uma integração não estiver disponível, faça a preparação local ou análise da configuração. Isso prepara a prática, mas a competência de execução fica pendente até ser demonstrada. Não é necessário acessar clientes, comprar outro plano ou publicar dados reais.
