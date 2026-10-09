# 07 — Executar Claude Code em automação e CI

**Fase:** 6. **Tópico:** `topic_cc_ci`.

**Pré-requisito:** testes determinísticos, acesso a um repositório de prática e conhecimento de consumo e permissões.

## Conceito

Modo não interativo permite integrar Claude Code a scripts. A automação precisa interpretar sucesso, falha e saída inválida. O agente pode analisar código; a aprovação da entrega ainda depende dos critérios, testes e revisão.

Consulte [execução programática](https://code.claude.com/docs/en/headless), [CLI](https://code.claude.com/docs/en/cli-reference) e [GitHub Actions](https://code.claude.com/docs/en/github-actions).

## Prática

1. Comece com um pedido curto e de análise, por exemplo `claude -p "Explique os critérios para revisar uma função que consolida CSV."`. Confira autenticação, permissões e consumo antes de executar.
2. Evolua para analisar um diff de prática com formato estruturado. Confira as opções de saída disponíveis com `claude --help`; valide o envelope e o conteúdo, sem assumir que uma resposta textual sempre é JSON válido.
3. Escreva um wrapper que capture stdout, stderr e código de saída. Teste sucesso, resposta incompleta e erro da execução. Se usar respostas simuladas para testar o wrapper, diferencie-as da execução real.
4. Faça um workflow de CI para os testes Python, independente do agente. Provoque uma falha controlada e demonstre o status do pipeline.
5. Em repositório de prática, prepare uma etapa ou workflow separado de análise com Claude Code, usando a integração oficial atual. Restrinja eventos, acesso e credenciais ao necessário; não conceda secrets a código não confiável.
6. Execute uma análise sobre um evento controlado. Revise logs para confirmar resultado sem expor credenciais. Registre o que ocorre se autenticação, rede ou análise falhar.
7. Evite merge automático como requisito do exercício. Use o relatório como insumo à revisão e registre pendências visíveis quando o agente não estiver disponível.

## Entrega e aceite

Wrapper, workflow, logs de sucesso e falha e `projects/cli-e-ci/entrega.md`. Separe evidência de execução real de fixtures simuladas. Um workflow escrito, mas não executado, é preparação: a competência permanece pendente.

## Tentativa autônoma e transferência

Adapte a automação para outro evento ou repositório. Explique o limite entre testes determinísticos e parecer do agente, e mostre como a falha evita uma aprovação sem verificação.

**Alternativa de acesso:** se o aluno não tiver credenciais de CI para Claude Code, valide o wrapper e os testes locais e registre a demonstração externa pendente, sem exigir compra de um plano.
