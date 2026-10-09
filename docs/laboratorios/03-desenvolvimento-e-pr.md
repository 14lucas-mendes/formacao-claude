# 03 — Implementar, testar, depurar e entregar

**Fase:** 3. **Tópicos:** `topic_python_qualidade`, `topic_verificacao_saidas`, `topic_cc_debugging`, `topic_cc_git_pr`.

**Pré-requisito:** plano verificável, branch de prática e Python 3.11+.

## Conceito

Um teste representa comportamento esperado independentemente do código produzido. Debugging começa por uma diferença reproduzível entre esperado e observado. A PR registra uma mudança revisável; seu tamanho e suas evidências precisam permitir que outra pessoa a avalie.

## Contrato da automação

Crie uma função Python que leia CSV de ocorrências e consolide minutos de ocorrências `finalizada` por equipamento:

- Duração zero em um registro `finalizada` é válida e o equipamento deve aparecer no resultado com zero se não tiver outros minutos finalizados.
- Registros `aberta` são válidos, mas não entram na soma. Equipamentos com apenas registros `aberta` são omitidos; um arquivo com somente ocorrências abertas produz resultado vazio.
- Duração deve ser um inteiro não negativo; campos obrigatórios não podem estar vazios.
- IDs duplicados e estados desconhecidos devem gerar erro claro.
- Validação é feita antes da consolidação; a política inicial é falhar com linha e motivo, sem produzir relatório parcial.

Use os [dados fictícios](../../projects/dados/README.md). Calcule primeiro à mão o resultado do arquivo válido. O arquivo inválido reúne casos para testes separados; não exija que um único erro revele todos eles.

## Prática

1. Defina exemplos pequenos e o esperado antes de pedir implementação. Crie testes para soma, finalizada com duração zero, arquivo sem registros, equipamento com apenas ocorrências abertas em um arquivo misto, arquivo com somente ocorrências abertas e entradas inválidas.
2. Colabore com Claude Code em funções pequenas; execute testes e revise o diff. Sugestão com biblioteca padrão: `python3 -m unittest discover -s tests -v`.
3. Explique uma função gerada e escreva autonomamente uma função auxiliar e seu teste. Testes que só copiam a lógica da implementação não bastam.
4. Em uma branch descartável, introduza um defeito de filtragem que descarte duração zero. Reproduza a falha, formule uma hipótese e corrija. O teste de regressão deve falhar no código defeituoso e passar após a correção.
5. Faça uma pequena refatoração e execute novamente os testes relevantes.
6. O aluno revisa e produz o commit. Abra uma PR no repositório de prática com comportamento, comandos, resultados e limitações. Não faça merge só para cumprir o exercício.

## Entrega e aceite

Código, testes determinísticos e PR; `projects/desenvolvimento-e-pr/entrega.md` com esperado manual, reprodução do bug, resultado antes/depois e revisão de pelo menos um ponto encontrado no diff.

## Tentativa autônoma e transferência

Adapte uma função para os dados de inspeções, com testes próprios. Investigue outro defeito, por exemplo aceitar minutos negativos. Revise uma segunda alteração e justifique uma decisão de manter ou pedir ajuste.

**Falha a observar:** o agente afirma sucesso sem executar testes ou muda o contrato para fazê-los passar. Confira o contrato e a saída dos comandos.
