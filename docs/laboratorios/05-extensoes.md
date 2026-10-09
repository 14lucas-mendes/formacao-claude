# 05 — Construir e verificar extensões

**Fase:** 5, parte 1. **Tópicos:** `topic_skills`, `topic_integracoes`, `topic_hooks_permissoes`.

**Pré-requisito:** workflow testado e práticas de acesso exercitadas. Use o repositório de prática; não altere a skill do tutor.

## Conceito

Skill descreve um procedimento; MCP oferece ferramentas; hook reage a um evento. Escolha pelo efeito necessário e verifique o comportamento real. Extensões podem executar código e usar credenciais, portanto sua origem e escopo fazem parte da revisão.

Referências: [skills](https://code.claude.com/docs/en/skills), [MCP](https://code.claude.com/docs/en/mcp), [hooks](https://code.claude.com/docs/en/hooks-guide) e [plugins](https://code.claude.com/docs/en/plugins).

## Prática

1. Crie `.claude/skills/revisar-automacao/SKILL.md` no projeto de prática, com nome, descrição, critérios de revisão e modo de uso. O procedimento deve conferir contrato, testes e diff, sem publicar ou fazer merge.
2. Invoque a skill em duas alterações distintas. Registre um achado confirmado e um que você refutou. Corrija uma instrução ambígua.
3. Revise o conteúdo de um plugin ou a estrutura de empacotamento oficial. Explique o que seria distribuído e executado; instalação de terceiros é dispensável.
4. Escolha um servidor MCP de origem confiável, local ou já disponível, com leitura sobre dados fictícios. Confira configuração, escopo e ferramentas; realize uma consulta e compare com a fonte.
5. Provoque indisponibilidade ou acesso negado de maneira controlada. Registre diagnóstico e recuperação. Caso não tenha MCP disponível, prepare e revise a configuração, deixando a execução pendente.
6. Crie um hook de comando simples para um evento escolhido, por exemplo registrar a conclusão de um teste sem publicar nada. Use o formato da documentação atual, confira entrada e retorno e observe uma execução.
7. Teste a falha do comando do hook e uma regra de permissão com arquivos fictícios. Registre se a ação foi bloqueada, apenas notificada ou ignorada; não suponha garantia universal.

## Entrega e aceite

Skill, configuração sem credenciais, script de hook e `projects/extensoes/entrega.md` com invocações, resultado conferido do MCP e testes de sucesso/falha. Use configurações de escopo local quando a experiência não deva alterar todos os projetos.

## Tentativa autônoma e transferência

Para uma nova necessidade, escolha entre instrução, skill, MCP, hook e permissão. Adapte sua skill e seu hook a outra tarefa. Explique quais comportamentos foram comprovados e quais permanecem dependentes de acesso ou ferramenta.
