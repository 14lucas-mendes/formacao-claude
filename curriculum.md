# Currículo: Claude Code, Python e agentes de IA para transição de carreira

<!-- Itens são adicionados pelo workflow de currículo com IDs estáveis. -->

**Contexto:** empregado público (CLT) no setor de manutenção de uma empresa de transporte ferroviário, em transição para automação, agentes de IA e desenvolvimento de software, começando por Python. O aluno declarou que pode ter renda extra e que pode usar informações da empresa no próprio workflow com Claude.

**Objetivo (5 meses, até 2027-02-28):** concluir a **primeira etapa** da transição:
1. até o **marco de 2026-12-31**, usar Claude Code e o ecossistema Claude no trabalho diário de forma segura, verificável e documentada;
2. escrever, testar e revisar automações em Python e um agente simples com a API do Claude;
3. publicar 1–2 projetos de portfólio no GitHub voltados a manutenção;
4. apresentar uma primeira oferta de serviço a pelo menos um cliente potencial.

**Fora do escopo:** construir produto/SaaS próprio; aprofundamento técnico em MCP, hooks e plugins além do necessário para usar e decidir.

**Orçamento de tempo:** 4 h/semana × ~22 semanas ≈ 88 h, em sessões de ~1 h, preferencialmente no fim de semana. As semanas 12–13 caem nas festas de fim de ano: se você não estudar nelas, a semana de folga (22) cobre.

**Regra de conclusão:** um item só é marcado quando o tópico atinge domínio 80 (explicação Feynman autônoma + aplicação autônoma + aplicação transferida para novo contexto), com IDs de evidência registrados no `session-log.md`. Ler conteúdo, receber explicação ou ter código gerado pela IA não conta como evidência; conta o que você explica, escreve, testa ou corrige.

**Prioridade realista:** os itens com ★ são o núcleo e devem chegar a 80. Os itens **básico** têm meta 60: saber explicar e aplicar uma vez num caso real, sem transferência obrigatória.

**Fio condutor:** os mesmos problemas de manutenção atravessam as fases. A tarefa escolhida na Fase 2 vira automação em Python na Fase 4 e projeto de portfólio na Fase 5.

**Fontes primárias:** documentação do Claude Code (https://code.claude.com/docs), da plataforma Claude/API (https://platform.claude.com/docs) e central de ajuda (https://support.claude.com). Fontes específicas são registradas por lição via `/sources`.

---

## Fase 1: Fundamentos do Claude Code (semanas 1–3, ~12 h)

Capacidade observável: conduzir uma tarefa real no Claude Code sabendo o que ele está fazendo, por que, e como desfazer.

- [ ] ★ `topic_cc_modelo_mental`: Modelo mental do Claude Code: loop agêntico, ferramentas, contexto e limites
  - Evidências: Feynman (explicar o ciclo pedido → plano → ferramentas → verificação); aplicação (conduzir uma tarefa e narrar as decisões do agente); transferência (prever o comportamento numa tarefa diferente).
- [ ] ★ `topic_cc_contexto`: Contexto e instruções: CLAUDE.md, rules (`.claude/rules`), auto memory, /clear e /compact
  - Inclui o básico de **rules**: arquivos `.claude/rules/*.md`, opcionalmente limitados a caminhos via `paths`; diferença entre CLAUDE.md, rules, skills e memória.
  - Entrega: um `CLAUDE.md` útil escrito por você para um repositório real seu.
- [ ] ★ `topic_cc_seguranca`: Trabalho seguro: modos de permissão, revisão de diffs, Git como rede de segurança, dados sensíveis
  - Entrega: checklist pessoal de segurança aplicado a uma tarefa real, com um commit revisado por você.

## Fase 2: Ecossistema Claude no trabalho de manutenção (semanas 4–7, ~16 h)

Capacidade observável: escolher o ambiente certo para cada tarefa e ter uma tarefa recorrente da manutenção feita com IA, com tempo medido antes e depois.

- [ ] ★ `topic_escolha_ambiente`: Mapa do ecossistema Claude e escolha do ambiente: Chat, Projects, Cowork, Claude in Chrome, Claude Code (terminal, desktop, nuvem)
  - Evidência: para 3 tarefas reais, escolher o ambiente e justificar; transferência com uma tarefa nova.
  - Atenção: disponibilidade de alguns recursos (ex.: Claude in Chrome, uso do computador no Cowork) depende do plano e do sistema operacional; verificar na sua conta.
- [ ] **básico** `topic_cowork_projects`: Cowork e Projects no trabalho: projeto com instruções e arquivos, conectores, modos de permissão e tarefas agendadas
  - Entrega: um Project para a manutenção (ex.: manuais, procedimentos, histórico de falhas) e uma tarefa real executada no Cowork.
- [ ] ★ `topic_workflow_trabalho`: Automatizar uma tarefa recorrente da manutenção com processo documentado e medido
  - Exemplos: relatório de falhas, consolidação de ordens de serviço, indicadores (MTBF/MTTR), checklists de inspeção.
  - Entrega: processo em Markdown dentro de `projects/` + medição de tempo antes/depois.
- [ ] ★ `topic_verificacao_saidas`: Verificar saídas de IA: critérios de aceitação, checagem de fatos, testes
  - Evidência: detectar erros plantados numa saída técnica e definir critérios de aceitação antes de pedir.

## Fase 3: Extensões: skills, MCP, hooks e rules (semanas 8–9, ~8 h)

Capacidade observável: diante de uma necessidade, decidir se ela pede instrução (CLAUDE.md/rule), skill, conector/MCP, hook ou permissão, e aplicar o básico de cada um.

- [ ] **básico** `topic_skills`: Skills e plugins: quando criar, estrutura de SKILL.md, manutenção e reutilização
  - Aplicação: uma skill para o workflow da Fase 2. Plugins apenas como conceito: pacote que distribui skills, hooks e servidores MCP juntos.
- [ ] **básico** `topic_integracoes`: MCP e conectores: o que são, como conectar, permissões, riscos e custos
  - Aplicação: conectar um serviço que você já usa (ex.: Google Drive, Gmail, Notion) e executar uma tarefa real com ele.
- [ ] **básico** `topic_hooks_permissoes`: Hooks e regras de permissão: quando usar instrução, hook ou permissão (orientação vs garantia)
  - Ideia central: CLAUDE.md e rules orientam, mas não garantem; hooks e regras de permissão (`allow`/`deny` em `settings.json`) são aplicados pelo cliente.
  - Aplicação: um hook simples ou uma regra `deny` num repositório seu.

## Fase 4: Python e agentes, o novo núcleo (semanas 10–16, ~28 h)

Capacidade observável: escrever, testar e explicar código Python próprio, revisar criticamente código gerado pela IA e construir um agente simples com a API do Claude.

- [ ] ★ `topic_python_qualidade`: Python com testes, Git e leitura crítica de código gerado por IA
  - Evidência: escrever uma função com testes sem ajuda; encontrar e corrigir um bug plantado em código gerado por IA; explicar linha a linha um trecho gerado.
- [ ] ★ `topic_automacao_python`: Automações em Python para problemas de manutenção, construídas e testadas com Claude Code
  - Entrega: script em `projects/<slug>/` que resolve a tarefa da Fase 2 (ex.: ler planilha de OS, calcular indicadores, gerar relatório), com teste executado e resultado registrado.
- [ ] ★ `topic_agentes_api`: Agente simples com a API do Claude: chamada, tool use e loop agêntico
  - Entrega: agente em Python com 1–2 ferramentas próprias (ex.: consultar histórico de falhas, buscar no manual) e explicação de quando um agente é melhor que um script simples.

## Marco do mês 3: revisão de uso diário (semana 13, até 2026-12-31, ~1 h dentro da Fase 4)

Checagem com `/progress` e `/review`: os tópicos ★ das Fases 1–2 devem estar em 80 e o workflow da Fase 2 em uso real no trabalho. Se não estiverem, o atraso é registrado aqui e a Fase 3 é a primeira a ser comprimida.

## Fase 5: Portfólio e primeira oferta (semanas 17–21, ~20 h)

Capacidade observável: projetos públicos que um recrutador ou cliente entende sem você explicar, e uma oferta concreta validada com pessoas reais.

- [ ] ★ `topic_portfolio`: Portfólio: 1–2 projetos no GitHub com README voltados a manutenção
  - Entrega: repositório público com problema, solução, como rodar, testes e limitações; **sem dados internos da empresa** (use dados fictícios ou anonimizados no que for público).
- [ ] ★ `topic_nicho_problema`: Nicho em automação para manutenção industrial: problema validado em conversas reais
  - Evidência: notas de pelo menos 3 conversas com potenciais clientes.
- [ ] ★ `topic_oferta_servico`: Desenhar a oferta: escopo, entregáveis, preço, riscos, LGPD e responsabilidades
  - Entrega: proposta de uma página.
- [ ] ★ `topic_piloto_cliente`: Executar piloto ou apresentar proposta a um cliente potencial e registrar aprendizados

## Semana 22: folga e revisão final (~4 h)

Recupera atrasos ou faz a revisão espaçada final. Não é espaço para novos tópicos. Inclui planejar a **segunda etapa** da transição.

---

## Fontes verificadas (acesso em 2026-10-01)

- Claude Code Docs: How Claude remembers your project (CLAUDE.md, `.claude/rules/`, auto memory): https://code.claude.com/docs/en/memory
- Claude Code Docs: Extend Claude with skills: https://code.claude.com/docs/en/skills
- Claude Code Docs: Connect Claude Code to tools via MCP: https://code.claude.com/docs/en/mcp
- Claude Code Docs: Automate actions with hooks: https://code.claude.com/docs/en/hooks-guide
- Claude Code Docs: Configure permissions: https://code.claude.com/docs/en/permissions
- Claude Code Docs: Plugins overview: https://code.claude.com/docs/en/plugins/overview
- Claude Code Docs: Desktop application: https://code.claude.com/docs/en/desktop
- Claude Code Docs: Agent SDK overview: https://code.claude.com/docs/en/agent-sdk/overview
- Claude Platform Docs: Tool use overview: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
- Claude Help Center: Get started with Claude Cowork: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- Claude Help Center: Get started with Claude in Chrome: https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome

## Revisões do roadmap

- 2026-10-01 (rev. 4): o aluno informou que está em transição de carreira (manutenção ferroviária → automação, agentes de IA e desenvolvimento, começando por Python), que é CLT, que pode ter renda extra e que pode usar informações da empresa no próprio workflow. Mantidos 5 meses e ≈ 88 h:
  - nova Fase 4 "Python e agentes" (★): `topic_python_qualidade`, `topic_automacao_python` (promovido), `topic_agentes_api`;
  - nova Fase 5 "Portfólio e primeira oferta", com `topic_portfolio` (★) antes do nicho e da oferta;
  - nicho direcionado a manutenção industrial; workflow da Fase 2 direcionado a tarefas de manutenção;
  - Fase 2 de 5 para 4 semanas; Fase 3 de 4 para 2 semanas, toda em meta básica (`topic_skills` deixa de ser ★);
  - marco de 2026-12-31 mantido, agora dentro da Fase 4. Nenhuma evidência existia.
- 2026-10-01 (rev. 3): pedido do aluno para estender o plano de 3 para 5 meses (prazo 2027-02-28, 4 h/semana mantidas, ≈ 88 h). Mantido 2026-12-31 como marco do uso diário; Fase 2 de 4 para 5 semanas; Fase 3 de 2 para 4 semanas; `topic_automacao_python` volta a básico; Fase 4 de 4 para 8 semanas; incluídas uma semana de revisão (13) e uma de folga (22). Nenhuma evidência existia.
- 2026-10-01 (rev. 2): pedido do aluno para incluir o básico de skills, MCP, hooks e rules e o ecossistema do app (Projects, Cowork, Claude in Chrome). Sem aumentar o orçamento de 52 h:
  - rules incorporadas a `topic_cc_contexto`; ecossistema incorporado a `topic_escolha_ambiente`; plugins incorporados a `topic_skills`;
  - `topic_integracoes` focado em MCP e conectores;
  - novos tópicos básicos: `topic_cowork_projects` e `topic_hooks_permissoes`;
  - Fase 2 ganha uma semana; Fase 3 cai para 2 semanas; `topic_automacao_python` passa a opcional.
  - Nenhuma evidência existia; nenhum histórico foi perdido.
- 2026-10-01 (rev. 1): currículo inicial criado no setup. Nenhuma evidência ou domínio registrado.
