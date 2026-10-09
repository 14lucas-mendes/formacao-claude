# Guia de trabalho profissional com Claude Code

Use este guia junto dos [laboratórios](laboratorios/README.md). Claude Code opera sobre arquivos e ferramentas; você define resultado, limites e como verificar a entrega. [Visão geral oficial](https://code.claude.com/docs/en/overview).

## 1. Preparar o ambiente

Instale pela [documentação oficial](https://code.claude.com/docs/en/setup), autentique com o acesso autorizado e execute `claude --version` e `claude doctor`. Abra o agente na raiz correta do projeto. Confira Git, dependências e comandos de teste antes de delegar trabalho.

Registre sistema, shell, editor e versão. Terminal e integrações com editor são superfícies do Claude Code; escolha pelo fluxo de desenvolvimento e confira diferenças de disponibilidade. Use a integração com seu editor para localizar referências e revisar alterações; não é necessário comprar outra ferramenta para fazer os exercícios.

## 2. Definir uma tarefa verificável

Um pedido útil identifica problema, entradas, comportamento esperado, arquivos de referência, restrições e verificação. Não peça apenas “melhore o projeto”. Preencha o [registro de entrega](templates/entrega.md) antes de uma mudança maior.

Exemplo para o laboratório:

> Examine o tratamento de ocorrências e os testes. Quero consolidar duração por equipamento, incluindo duração zero. Duração negativa e campos obrigatórios vazios devem produzir erro claro. Primeiro proponha o plano e os casos de teste; depois implemente a mudança aprovada e apresente os resultados.

Para tarefas maiores, separe exploração, plano, implementação e revisão. Para uma correção pequena e bem delimitada, reduza a cerimônia. [Referência de práticas](https://code.claude.com/docs/en/best-practices).

## 3. Explorar e planejar

Comece com `claude --permission-mode plan`. Peça ao agente para localizar entradas, dependências, testes e padrões relevantes. Verifique os arquivos citados e transforme as suposições em perguntas ou experimentos.

O plano deve nomear arquivos, etapas, casos de erro e comando de verificação. Leia-o antes de autorizar alterações. Um plano não comprova que os testes existem nem que a implementação funcionará. [Opções da CLI](https://code.claude.com/docs/en/cli-reference).

## 4. Organizar contexto

Mantenha em `CLAUDE.md` apenas instruções duráveis: comandos que o agente precisa conhecer, convenções e restrições específicas. Use rules para orientações por área; skills para procedimentos reutilizáveis; memória para aprendizados que mereçam continuidade. Verifique quais arquivos foram carregados.

Uma sessão extensa exige seleção de contexto. Faça um registro de retomada antes de limpar ou compactar a conversa, contendo objetivo, branch, arquivos, verificações e próximo passo. Peça que uma nova sessão confirme o registro contra os arquivos reais. [Memória e instruções](https://code.claude.com/docs/en/memory).

## 5. Controlar acesso e desfazer

Revise o modo e as regras de permissão efetivos; configurações pessoais, locais, do projeto e da organização podem ter precedências distintas. Teste uma regra com arquivos fictícios e observe o resultado. Instruções em Markdown orientam comportamento; não constituem uma barreira de acesso.

Permissões de ferramentas e sandbox do shell têm escopos diferentes. Uma regra para leitura de arquivo não é uma promessa de bloquear todos os meios de ler o mesmo dado. Examine também comandos, rede e ferramentas externas. [Permissões](https://code.claude.com/docs/en/permissions), [configurações](https://code.claude.com/docs/en/settings) e [sandbox](https://code.claude.com/docs/en/sandboxing).

Antes de editar, confira `git status` e crie uma branch. Revise `git diff` e preserve o trabalho existente. Checkpoints da sessão ajudam a voltar sobre alterações rastreadas; não substituem Git nem revertem todos os efeitos de comandos e serviços externos. [Limites dos checkpoints](https://code.claude.com/docs/en/checkpointing).

## 6. Implementar, depurar e revisar

Trabalhe em mudanças pequenas. Para um bug, reproduza a falha e descreva esperado versus observado. Formule uma hipótese, rode um experimento e aplique a menor correção sustentada pelos resultados. Crie um teste de regressão que falhe antes e passe depois.

Faça revisão humana do diff. Procure erros de borda, tratamento de falhas, alterações fora do escopo e testes que só repetem o código. Execute o comando real; registre resultado e limitações. Uma resposta dizendo “testes passaram” precisa de evidência.

A PR deve explicar problema, comportamento resultante, verificação e riscos restantes. O aluno deve conseguir explicar as decisões, mesmo quando Claude Code produziu o código. [Fluxos comuns](https://code.claude.com/docs/en/common-workflows).

## 7. Reutilizar e integrar

| Necessidade | Recurso a avaliar | Verificação |
| --- | --- | --- |
| Convenção do repositório | CLAUDE.md ou rule | Instrução carregada e aplicada |
| Procedimento repetido | Skill | Invocação em duas tarefas distintas |
| Acesso a ferramenta ou fonte externa | MCP | Ferramentas e acesso efetivo conhecidos |
| Ação ligada a um evento | Hook | Evento, entrada, resultado e falha testados |
| Investigação delimitada | Subagente | Escopo, ferramentas e conclusão conferidos |
| Sessões editando tarefas distintas | Worktree | Branches separadas e integração revisada |
| Compartilhar extensões entre projetos | Plugin | Origem e conteúdo revisados |

Skills instruem procedimentos. Hooks executam ações em eventos; seus comandos também podem falhar e ter efeitos colaterais. MCP expõe ferramentas, não garante que os resultados sejam corretos. Um subagente precisa de uma tarefa delimitada e revisão da saída; delegação não transfere sua responsabilidade pela entrega.

Consulte os exemplos e formatos atuais em [skills](https://code.claude.com/docs/en/skills), [hooks](https://code.claude.com/docs/en/hooks-guide), [MCP](https://code.claude.com/docs/en/mcp), [subagentes](https://code.claude.com/docs/en/sub-agents) e [plugins](https://code.claude.com/docs/en/plugins).

## 8. Medir consumo e automatizar

Registre tempo até uma entrega aceita, retrabalho e uso disponível na conta. Escolha o modelo pelo problema e pela qualidade necessária, e repita uma tarefa comparável antes de concluir que houve ganho. Consumo de assinatura e faturamento da API não são equivalentes; não trate uma estimativa de sessão como fatura. [Custos e consumo](https://code.claude.com/docs/en/costs).

O modo `claude -p` executa um pedido sem conversa interativa. Comece por análise com saída estruturada; valide a saída, o código de retorno e o comportamento em falha. As permissões continuam relevantes. Considere um teto de gasto quando suportado, mas não o trate como limite exato de faturamento. [Execução programática](https://code.claude.com/docs/en/headless).

Em CI, separe testes determinísticos da análise pelo agente. Use credenciais pelo mecanismo de secrets do serviço e não as exponha a código ou eventos não confiáveis. Revise permissões do workflow, origem do evento e logs. Faça a primeira execução em um repositório de prática; indisponibilidade do agente deve resultar em falha visível ou revisão humana pendente. [GitHub Actions](https://code.claude.com/docs/en/github-actions).

## 9. Diagnosticar problemas de uso

| Sintoma | Primeira investigação |
| --- | --- |
| CLI não encontrado | Instalação, PATH, versão e diagnóstico |
| Agente atua no projeto errado | Diretório atual e raiz do repositório |
| Instrução ignorada | Arquivo carregado, escopo e conflito de regras |
| Comando ou rede negados | Regra efetiva e ambiente, sem desativar controles às cegas |
| Hook não dispara | Evento, configuração carregada, entrada e resultado |
| Sessão perde o objetivo | Contexto, checkpoint e tamanho da tarefa |
| “Resolvido” sem evidência | Reprodução, teste e comando de verificação |

Reproduza em um caso mínimo e registre o que observou. Diferencie erro de instalação, configuração, ferramenta, permissão e código antes de mudar várias coisas ao mesmo tempo.
