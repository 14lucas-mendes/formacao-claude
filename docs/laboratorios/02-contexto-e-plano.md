# 02 — Ler, planejar e retomar um projeto

**Fase:** 2. **Tópicos:** `topic_cc_contexto`, `topic_cc_planejamento`, `topic_cc_sessoes`.

**Pré-requisito:** primeira tarefa supervisionada e revisão de diff.

## Conceito

Instruções duráveis, contexto da tarefa e registro de retomada resolvem necessidades distintas. CLAUDE.md orienta sessões; o pedido delimita a mudança; o checkpoint registra o estado do trabalho. Uma conversa anterior não é a fonte definitiva sobre os arquivos atuais.

Consulte [memória](https://code.claude.com/docs/en/memory), [CLI](https://code.claude.com/docs/en/cli-reference) e [checkpoints](https://code.claude.com/docs/en/checkpointing).

## Prática

1. Escolha um pequeno repositório existente e execute seus testes de referência. Pode ser uma automação sua; se não existir, use os scripts do tutor apenas para leitura, sem modificar sua cópia.
2. Inicie `claude --permission-mode plan`. Peça entradas, dependências, comandos e testes relevantes. Confira três referências citadas nos arquivos reais.
3. Escreva no repositório de prática um CLAUDE.md curto com comandos e convenções; acrescente uma rule com escopo adequado. Observe quais instruções são carregadas.
4. Planeje a consolidação dos [dados de ocorrências](../../projects/dados/README.md): saídas, casos inválidos, testes e arquivos a alterar. Identifique uma suposição ainda não verificada.
5. Introduza uma ambiguidade controlada numa instrução de prática, observe o efeito e corrija a redação. Não copie toda a documentação para CLAUDE.md.
6. Escreva um checkpoint pelo [modelo](../templates/entrega.md), encerre a sessão e retome em outra. Confirme branch, alterações locais e próximo passo contra os arquivos.
7. Experimente limpar ou compactar contexto após salvar o checkpoint. Compare o que permanece disponível; não faça isso na sessão histórica do tutor como parte do experimento.

## Entrega e aceite

`projects/contexto-e-plano/entrega.md`: mapa conferido, comandos de referência, instruções criadas, plano com critérios de aceitação, hipótese e registro de retomada. Não apresente o plano como código já implementado.

## Tentativa autônoma e transferência

Explique onde guardar uma convenção, um procedimento recorrente e um resultado de teste. Planeje uma alteração em outra área do projeto e retome após uma interrupção.

**Falha a observar:** o checkpoint declara um teste aprovado que não foi executado, ou aponta uma branch diferente. Corrija o registro com a evidência real e explique o limite dos checkpoints em comandos e serviços externos.
