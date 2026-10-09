# 04 — Manter uma automação e medir o trabalho

**Fase:** 4. **Tópicos:** `topic_workflow_trabalho`, `topic_automacao_python`, `topic_cc_custos`.

**Pré-requisito:** implementação e testes do laboratório 03.

## Conceito

Uma automação profissional precisa de um caminho repetível de uso e manutenção. Tempo economizado só tem significado quando o resultado é aceito. Compare tarefas semelhantes e registre retrabalho; poucas observações não comprovam ganho geral de produtividade.

Consulte [custos e consumo](https://code.claude.com/docs/en/costs) antes de comparar modelos e formas de acesso.

## Prática

1. Evolua a função do laboratório 03 para uma CLI com entrada CSV e relatório de saída determinístico. Argumentos ausentes, arquivo inexistente ou conteúdo inválido devem produzir mensagem útil e retorno diferente de zero.
2. Escreva README com comando de uso, exemplo fictício, testes e limitações. Execute a partir de um ambiente limpo e confirme que a saída não depende do seu diretório pessoal.
3. Registre o fluxo pedido → exploração → plano → implementação → teste → revisão → PR. Defina o que torna uma entrega aceitável.
4. Faça uma segunda PR acrescentando filtro opcional por equipamento. Sem filtro, preserve o resultado anterior; teste filtro existente, inexistente e entrada inválida.
5. Em duas tarefas pequenas de dificuldade parecida, registre tempo até aceite, intervenções, falhas e uso que a conta expõe. Se comparar modelos, confirme as opções disponíveis na sua versão.
6. Reduza contexto irrelevante e repita uma consulta equivalente. Descreva qualidade e consumo observado sem atribuir causalidade que a comparação não sustenta.

## Entrega e aceite

CLI, duas PRs, README reproduzível e `projects/automacao-e-custos/entrega.md`. Inclua tabela com tarefa, tempo, retrabalho, uso observado, versão/modelo e forma de acesso. Se um dado não estiver disponível, escreva isso. Não invente faturamento nem use estimativa de tokens como custo exato.

## Tentativa autônoma e transferência

Receba uma nova mudança de relatório e conduza o fluxo sem um plano fornecido pelo tutor. Justifique como escolher modelo, contexto e tamanho da tarefa em um repositório diferente.

**Falha a observar:** a CLI retorna sucesso apesar de falhar, ou a segunda PR altera o comportamento sem filtro. Demonstre um teste que detecte a regressão.
