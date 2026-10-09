# 06 — Delegar e integrar trabalho isolado

**Fase:** 5, parte 2. **Tópicos:** `topic_cc_subagentes`, `topic_cc_worktrees`.

**Pré-requisito:** Git, revisão de PR e tarefas delimitadas.

## Conceito

Um subagente executa uma investigação com escopo próprio; seu relatório precisa ser conferido. Um worktree fornece outro diretório de trabalho para uma branch. Separar diretórios ajuda a evitar edição concorrente, mas a integração ainda pode produzir conflitos ou incompatibilidades.

Referências: [subagentes](https://code.claude.com/docs/en/sub-agents) e [workflows](https://code.claude.com/docs/en/common-workflows).

## Prática

1. Defina duas tarefas independentes na automação: revisar testes de entrada inválida e melhorar a documentação. Diga quais arquivos pertencem a cada tarefa e qual resultado espera.
2. Crie um subagente em `.claude/agents/` no projeto de prática para leitura e revisão. Restrinja ferramentas ao necessário, confira a configuração efetiva e não inclua Bash como garantia de somente leitura: comandos de shell também podem escrever.
3. Peça relatório com caminhos e achados verificáveis. Confirme os achados e registre uma conclusão que exigiu ajuste.
4. Confira `git status`. Crie dois worktrees/branches usando Git ou o recurso da sua versão do Claude Code, e execute uma tarefa em cada diretório.
5. Inspecione diffs e testes separadamente, integre um trabalho por vez e rode a verificação combinada.
6. Em branches descartáveis, crie um conflito pequeno no README. Resolva preservando os dois requisitos; não use sobrescrita automática para “sumir” com o conflito.
7. Antes de remover worktrees, verifique mudanças não commitadas e commits ainda não integrados. Remova apenas os worktrees já conferidos, sem descarte forçado de trabalho.

## Entrega e aceite

Configuração do subagente, relatório conferido, branches ou commits das tarefas e `projects/trabalho-paralelo/entrega.md` com integração, conflito resolvido e testes.

## Tentativa autônoma e transferência

Decida se uma mudança interdependente merece execução paralela. Decomponha outro pedido, integre suas partes e explique quando delegar aumentaria custo ou risco sem benefício.

**Falha a observar:** duas sessões editam o mesmo diretório ou a integração passa em cada branch e falha no conjunto. Mostre como detectar e corrigir.
