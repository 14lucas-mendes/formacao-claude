# Currículo: formação profissional em Claude Code

**Objetivo:** conduzir entregas de software com Claude Code de forma profissional, verificável e reproduzível. A manutenção industrial é o cenário dos exercícios; Python serve à prática de desenvolvimento, sem transformar a trilha em um curso geral de linguagem ou API.

**Planejamento:** 26 semanas × 4 h = **104 h**; 100 h distribuídas nas fases e 4 h de recuperação. Mantidos o prazo **2027-03-31** e o marco de uso diário **2026-12-31** do estudo existente. As semanas são uma sequência de referência a partir do calendário original; em uma retomada tardia, reorganize com o aluno sem reduzir os critérios nem atribuir avanço pelo tempo decorrido. Uma semana de reserva cobre 4 h; duas semanas sem estudo exigem replanejar.

**Método:** sessões de cerca de 1 h, com resgate de pré-requisito, explicação curta, prática, tentativa autônoma e registro. O tutor retoma primeiro a sessão interrompida. O [guia profissional](docs/guia-profissional.md) apoia o método; as [fontes oficiais](docs/fontes.md) sustentam os recursos.

## Conclusão e evidência

Todo item obrigatório abaixo exige **domínio 80**, segundo o contrato da skill: explicação Feynman autônoma, aplicação autônoma independente e aplicação transferida a novo contexto. A entrega específica também deve existir, com IDs de evidência no estado e em `session-log.md`.

Autonomia significa o aluno decidir, justificar, verificar e corrigir sem receber a resposta da avaliação. Trabalhar com Claude Code é parte da competência; simplesmente aceitar código ou repetir uma explicação fornecida não é evidência. Os laboratórios não vêm resolvidos. Tentativas assistidas continuam registráveis segundo a matriz, mas não atendem aos requisitos de 60 ou 80.

Um tópico só recebe checkbox concluído após essa avaliação. Familiarização opcional pode ter meta 60, mas não equivale a concluir o tópico nem a formação. Todos os itens começam abertos nesta revisão.

**Fio condutor:** evoluir uma automação de ocorrências com dados fictícios, revisar o código, tratar um bug, incorporar um requisito novo e entregar por PR. Não exige uso de dados internos, contratar cliente ou vender serviço.

## Mapa da trilha

| Fase | Semanas | Horas | Entrega principal |
| --- | --- | --- | --- |
| 1. Fundamentos e ambiente | 1–3 | 12 | [Laboratório](docs/laboratorios/01-ambiente.md) |
| 2. Contexto, planejamento e continuidade | 4–6 | 12 | [Laboratório](docs/laboratorios/02-contexto-e-plano.md) |
| 3. Desenvolvimento, testes, debugging e PR | 7–11 | 20 | [Laboratório](docs/laboratorios/03-desenvolvimento-e-pr.md) |
| 4. Automação e produtividade | 12–15 | 16 | [Laboratório](docs/laboratorios/04-automacao-e-custos.md) |
| 5. Extensões e trabalho paralelo | 16–20 | 20 | [Laboratório](docs/laboratorios/05-extensoes.md) |
| 6. Execução não interativa e CI | 21–23 | 12 | [Laboratório](docs/laboratorios/07-cli-e-ci.md) |
| 7. Projeto integrador e avaliação | 24–25 | 8 | [Laboratório](docs/laboratorios/08-projeto-integrador.md) |
| Recuperação e revisão final | 26 | 4 | Lacunas e revisão espaçada |
| **Total** | **26** | **104** | Competência demonstrada |

## Fase 1: Fundamentos e ambiente (semanas 1–3, 12 h)

**Pré-requisito:** Conforto básico com terminal; diagnosticar lacunas de Git e Python na primeira sessão.

- [ ] `topic_cc_setup`: Instalação, autenticação, diagnóstico e integração com editor
  - Entrega e demonstração: Diagnosticar a instalação, registrar versão e acesso, abrir o projeto e usar a integração do editor; reproduzir a preparação em outro ambiente ou perfil.
- [ ] `topic_cc_modelo_mental`: Modelo mental do Claude Code: loop agêntico, ferramentas, contexto e limites
  - Entrega e demonstração: Explicar o ciclo pedido → ferramenta → observação → nova ação; identificar cada etapa numa tarefa e prever comportamento em outra.
- [ ] `topic_escolha_ambiente`: Superfícies do Claude Code: terminal, editor e execução remota
  - Entrega e demonstração: Escolher uma superfície do Claude Code para duas tarefas e justificar acesso ao repositório, revisão e limitações; não exige estudar Cowork ou Chat.
- [ ] `topic_cc_seguranca`: Permissões, sandbox, revisão de diffs, Git e dados sensíveis
  - Entrega e demonstração: Aplicar e testar permissões em dados fictícios, revisar um diff e demonstrar recuperação de uma mudança sem perder trabalho existente.

**Prática:** [01-ambiente](docs/laboratorios/01-ambiente.md).

## Fase 2: Contexto, planejamento e continuidade (semanas 4–6, 12 h)

**Pré-requisito:** Conduzir uma tarefa simples, reconhecer ferramentas e revisar alterações.

- [ ] `topic_cc_contexto`: Contexto e instruções: CLAUDE.md, rules, memória e seleção de arquivos
  - Entrega e demonstração: Criar CLAUDE.md e uma rule útil no projeto de prática; mostrar o que carregou e corrigir uma instrução ambígua em outra tarefa.
- [ ] `topic_cc_planejamento`: Especificação, exploração de repositórios e Plan Mode
  - Entrega e demonstração: Produzir um mapa do repositório e plano com arquivos, dependências e critérios; detectar uma suposição incorreta antes de implementar.
- [ ] `topic_cc_sessoes`: Gestão de sessões: retomada, compactação e limites dos checkpoints
  - Entrega e demonstração: Interromper e retomar uma tarefa com checkpoint escrito, confirmar o estado real e explicar o que Git e checkpoints podem recuperar.

**Prática:** [02-contexto-e-plano](docs/laboratorios/02-contexto-e-plano.md).

## Fase 3: Desenvolvimento, testes, debugging e PR (semanas 7–11, 20 h)

**Pré-requisito:** Ter um plano verificável e contexto mínimo do projeto de prática.

- [ ] `topic_python_qualidade`: Leitura crítica e implementação Python com testes usando Claude Code
  - Entrega e demonstração: Explicar o código gerado, escrever uma função e teste de borda autonomamente e refatorar sem alterar o comportamento.
- [ ] `topic_verificacao_saidas`: Critérios de aceitação e verificação independente de código e saídas
  - Entrega e demonstração: Definir esperado antes de gerar código, detectar uma saída incorreta e usar teste independente; verificar um segundo caso não fornecido pelo tutor.
- [ ] `topic_cc_debugging`: Debugging: reprodução, hipóteses, correção e regressão
  - Entrega e demonstração: Reproduzir um bug, testar uma hipótese e entregar correção com teste que falhe antes e passe depois; repetir com falha diferente.
- [ ] `topic_cc_git_pr`: Branches, commits, revisão de código e pull requests
  - Entrega e demonstração: Preparar branch, revisar diff, produzir commit do aluno e PR com comandos e resultados; revisar também uma alteração de outra tarefa.

**Prática:** [03-desenvolvimento-e-pr](docs/laboratorios/03-desenvolvimento-e-pr.md).

## Fase 4: Automação e produtividade (semanas 12–15, 16 h)

**Pré-requisito:** Conseguir executar testes, detectar um bug e revisar uma PR.

- [ ] `topic_workflow_trabalho`: Workflow profissional de desenvolvimento documentado e medido
  - Entrega e demonstração: Registrar um procedimento repetível desde o pedido até a revisão; medir tempo e retrabalho com limites explícitos da comparação.
- [ ] `topic_automacao_python`: Automação Python de ocorrências construída, testada e mantida com Claude Code
  - Entrega e demonstração: Entregar CLI para dados fictícios, testes e README; aceitar mudança de requisito por uma segunda PR preservando comportamento anterior.
- [ ] `topic_cc_custos`: Escolha de modelos, gestão de contexto, consumo e produtividade
  - Entrega e demonstração: Registrar consumo disponível e tempo em duas tarefas comparáveis, justificar modelo e contexto, identificar onde a medição não permite concluir.

**Prática:** [04-automacao-e-custos](docs/laboratorios/04-automacao-e-custos.md).

## Fase 5: Extensões e trabalho paralelo (semanas 16–20, 20 h)

**Pré-requisito:** Workflow de desenvolvimento e automação verificáveis; práticas de acesso e retomada exercitadas.

- [ ] `topic_skills`: Skills e plugins: criação, teste, reutilização e distribuição
  - Entrega e demonstração: Criar e invocar uma skill em dois casos, verificar falhas e revisar um pacote de plugin; não exige instalar plugins de terceiros.
- [ ] `topic_integracoes`: MCP no Claude Code: escopos, ferramentas, configuração e falhas
  - Entrega e demonstração: Configurar ou inspecionar MCP de fonte confiável, executar uma leitura controlada e diagnosticar indisponibilidade ou acesso negado.
- [ ] `topic_hooks_permissoes`: Hooks e permissões: eventos, configuração e validação do comportamento
  - Entrega e demonstração: Criar hook de comando para um evento específico, testar sucesso e falha; demonstrar uma regra de permissão e explicar seu escopo.
- [ ] `topic_cc_subagentes`: Subagentes: delegação delimitada, ferramentas e revisão
  - Entrega e demonstração: Criar subagente para investigação delimitada, conferir ferramentas efetivas e verificar suas conclusões contra arquivos reais.
- [ ] `topic_cc_worktrees`: Worktrees e sessões paralelas: isolamento e integração
  - Entrega e demonstração: Executar tarefas distintas em worktrees separados, revisar e integrar branches, resolver um conflito controlado e encerrar sem perda.

**Prática:** [05-extensoes](docs/laboratorios/05-extensoes.md). Inclui também o [laboratório de subagentes e worktrees](docs/laboratorios/06-subagentes-e-worktrees.md); os dois dividem as 20 h desta fase.

## Fase 6: Execução não interativa e CI (semanas 21–23, 12 h)

**Pré-requisito:** Testes determinísticos e revisão manual funcionando; conhecer permissões e consumo.

- [ ] `topic_cc_ci`: Claude Code não interativo e CI: saída, falhas, credenciais e revisão
  - Entrega e demonstração: Executar análise não interativa, validar retorno e saída, e demonstrar CI em repositório de prática com sucesso e falha observáveis.

**Prática:** [07-cli-e-ci](docs/laboratorios/07-cli-e-ci.md).

## Fase 7: Projeto integrador e avaliação (semanas 24–25, 8 h)

**Pré-requisito:** Competências anteriores praticadas; usar as lacunas do tutor para priorizar revisão.

- [ ] `topic_portfolio`: Projeto integrador e portfólio: entrega reproduzível com Claude Code
  - Entrega e demonstração: Apresentar projeto executável com duas PRs e histórico de testes; resolver pedido novo autonomamente e explicar limites e manutenção.

**Prática:** [08-projeto-integrador](docs/laboratorios/08-projeto-integrador.md).

## Marco de uso diário (até 2026-12-31)

Revise com `/progress` e `/review` o uso real do Claude Code, os tópicos das Fases 1–3 e o fluxo da primeira automação. Busque entrega com plano, teste, diff revisado e retomada documentada. Se houver lacunas, registre o atraso e redistribua sessões com o aluno; não marque domínio automaticamente nem comprima segurança e verificação.

## Semana 26: recuperação e revisão (4 h)

Reveja as evidências e a retenção, repita uma tarefa em outro contexto e confira pendências do projeto. Se 4 h não bastarem, registre a necessidade de extensão. A conclusão não é garantida pelo prazo.

## Aprofundamento opcional

- `topic_agentes_api`: agente via API do Claude. Estudo posterior, fora das 104 h; meta inicial de familiarização 60 com explicação e aplicação autônomas. Exige verificar acesso e cobrança próprios. Usar Claude Code para desenvolver o agente é diferente de executar Claude Code.
- Empacotamento avançado de plugins, Agent SDK e recursos experimentais podem ser incluídos por pedido e com replanejamento; não bloqueiam o núcleo.

## Tópicos históricos fora do núcleo

Estes IDs continuam em `.ai-tutor/state.json` para preservar referências anteriores. Não entram nos requisitos de conclusão nem no próximo tópico automático:

| ID | Escopo anterior |
| --- | --- |
| `topic_cowork_projects` | Cowork e Projects no trabalho |
| `topic_nicho_problema` | Validação de nicho com clientes |
| `topic_oferta_servico` | Desenho de oferta comercial |
| `topic_piloto_cliente` | Piloto ou proposta a cliente |

## Revisão desta trilha

**2026-10-09 — versão curricular 6:** núcleo profissional de Claude Code, 21 competências obrigatórias, oito laboratórios, execução não interativa e CI, com registro de entregas. Acrescentados nove IDs; mantidos os 17 existentes, a sessão interrompida, o próximo foco e todo o histórico. Nenhuma evidência ou domínio foi criado. A configuração lista as trilhas em `curriculum_tracks`.

As revisões anteriores estão em [histórico curricular](docs/historico-curricular.md).
