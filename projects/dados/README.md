# Dados fictícios para os laboratórios

Os arquivos desta pasta são material de prática criado para a formação. Não contêm dados de uma empresa e não contam como entrega ou evidência do aluno.

| Arquivo | Finalidade |
| --- | --- |
| [ocorrencias-validas.csv](ocorrencias-validas.csv) | Soma, duração zero e estado aberto |
| [ocorrencias-invalidas.csv](ocorrencias-invalidas.csv) | Campo vazio, negativo, duplicidade e estado desconhecido |
| [inspecoes.csv](inspecoes.csv) | Transferência para outra estrutura e regra de negócio |

CSV usa UTF-8, vírgula e uma linha de cabeçalho. `duracao_minutos` e `minutos` são inteiros. Identificadores de OS, equipamentos e inspeções são inventados.

No arquivo de ocorrências inválidas, o registro OS101 se repete de propósito. Separe cada caso nos testes para observar todos os erros, pois o contrato inicial interrompe no primeiro erro.

Antes de gerar a implementação, calcule o esperado à mão para os arquivos válidos. Para inspeções, defina uma regra nova, como contar resultados por ativo e somar minutos apenas de inspeções com ajuste necessário. Declare o contrato antes de programar; ele não é automaticamente o mesmo das ocorrências.

Crie um terceiro conjunto pequeno sem ajuda do tutor para a avaliação de transferência. Preserve estes arquivos como referência.
