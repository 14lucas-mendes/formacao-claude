# 01 — Preparar e supervisionar o ambiente

**Fase:** 1. **Tópicos:** `topic_cc_setup`, `topic_cc_modelo_mental`, `topic_escolha_ambiente`, `topic_cc_seguranca`.

**Pré-requisito:** terminal, acesso ao Claude Code e um repositório descartável de prática.

## Conceito

Claude Code alterna decisões e uso de ferramentas a partir do pedido e do contexto disponível. Uma ferramenta produz uma observação que pode mudar o próximo passo. Você supervisiona o objetivo e confere o resultado; uma explicação convincente não comprova execução.

O diretório, a superfície de uso e as permissões influenciam o trabalho possível. [Instalação](https://code.claude.com/docs/en/setup) e [permissões](https://code.claude.com/docs/en/permissions).

## Prática

1. Registre sistema, shell, versão do CLI e forma de autenticação, sem copiar credenciais. Execute `claude --version` e `claude doctor`; resolva ou registre os diagnósticos.
2. Abra o repositório no terminal e no seu editor. Use a integração disponível do Claude Code para consultar um arquivo e inspecionar uma alteração. Compare o fluxo; se não houver integração disponível, registre a demonstração pendente.
3. Crie uma branch de prática e um arquivo de texto. Peça uma mudança pequena, veja as ferramentas usadas e revise o diff antes de manter a alteração.
4. Inspecione os modos e regras de permissão. Com um arquivo fictício sem informações reais, teste uma restrição e registre ferramenta, pedido e resultado. Explique quais acessos a regra cobre.
5. Faça uma alteração indesejada controlada e recupere o arquivo, preservando outro arquivo com trabalho não relacionado. Registre o método usado.

## Entrega e aceite

`projects/ambiente/entrega.md` deve conter diagnóstico, versão, diferenças entre superfícies, diff, teste da restrição e recuperação. Explique o loop agêntico usando as ações observadas. Não registre uma ferramenta apenas porque o agente disse que a usou.

## Tentativa autônoma e transferência

Sem receber uma resposta modelo, descreva o ciclo que Claude Code seguiria para transformar dados de ocorrências em relatório. Depois prepare outro repositório ou perfil e identifique uma diferença de contexto ou acesso. Demonstre recuperação de uma alteração diferente.

**Falha a observar:** o agente lê o diretório errado ou atua com uma regra que você supunha estar ativa. Mostre como localizar e corrigir a causa, sem desativar controles indiscriminadamente.
