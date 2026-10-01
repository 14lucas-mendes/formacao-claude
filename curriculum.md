# Currículo: Claude Code aplicado ao trabalho e a serviços com IA

<!-- Itens são adicionados pelo workflow de currículo com IDs estáveis. -->

**Objetivo (até 2026-12-31):** (1) usar Claude Code e o ecossistema Claude (Projects, Cowork, conectores, Claude in Chrome) no fluxo de trabalho diário de forma segura, verificável e documentada; (2) ter uma primeira oferta de serviço com IA definida, com piloto entregue ou proposta apresentada a pelo menos um cliente potencial.

**Fora do escopo:** construir produto/SaaS próprio; aprofundamento técnico em MCP, hooks e plugins além do necessário para usar e decidir.

**Orçamento de tempo:** 4 h/semana × ~13 semanas ≈ 52 h, em sessões de ~1 h, preferencialmente no fim de semana.

**Regra de conclusão:** um item só é marcado quando o tópico atinge domínio 80 (explicação Feynman autônoma + aplicação autônoma + aplicação transferida para novo contexto), com IDs de evidência registrados no `session-log.md`. Ler conteúdo ou receber explicação não conta como evidência.

**Prioridade realista:** com 52 h, os itens com ★ são o núcleo e devem chegar a 80. Os itens marcados **básico** têm meta 60: saber explicar e aplicar uma vez num caso real, sem transferência obrigatória. Itens **opcionais** só entram se sobrar tempo.

**Fontes primárias:** documentação oficial do Claude Code (https://code.claude.com/docs) e central de ajuda do Claude (https://support.claude.com). Fontes específicas são registradas por lição via `/sources`.

---

## Fase 1: Fundamentos operacionais (semanas 1–3, ~12 h)

Capacidade observável: conduzir uma tarefa real no Claude Code sabendo o que ele está fazendo, por que, e como desfazer.

- [ ] ★ `topic_cc_modelo_mental`: Modelo mental do Claude Code: loop agêntico, ferramentas, contexto e limites
  - Evidências: Feynman (explicar o ciclo pedido → plano → ferramentas → verificação); aplicação (conduzir uma tarefa e narrar as decisões do agente); transferência (prever o comportamento numa tarefa diferente).
- [ ] ★ `topic_cc_contexto`: Contexto e instruções: CLAUDE.md, rules (`.claude/rules`), auto memory, /clear e /compact
  - Inclui o básico de **rules**: arquivos `.claude/rules/*.md`, opcionalmente limitados a caminhos via `paths`; diferença entre CLAUDE.md, rules, skills e memória.
  - Entrega: um `CLAUDE.md` útil escrito por você para um repositório real seu, com pelo menos uma rule com escopo por caminho, se fizer sentido.
- [ ] ★ `topic_cc_seguranca`: Trabalho seguro: modos de permissão, revisão de diffs, Git como rede de segurança, dados sensíveis
  - Entrega: checklist pessoal de segurança aplicado a uma tarefa real, com um commit revisado por você.

## Fase 2: Ecossistema Claude no trabalho diário (semanas 4–7, ~14 h)

Capacidade observável: escolher o ambiente certo para cada tarefa e ter uma tarefa recorrente do trabalho feita com IA, com tempo medido antes e depois.

- [ ] ★ `topic_escolha_ambiente`: Mapa do ecossistema Claude e escolha do ambiente: Chat, Projects, Cowork, Claude in Chrome, Claude Code (terminal, desktop, nuvem)
  - Evidência: para 3 tarefas reais, escolher o ambiente e justificar; transferência com uma tarefa nova.
  - Atenção: disponibilidade de alguns recursos (ex.: Claude in Chrome, uso do computador no Cowork) depende do plano e do sistema operacional; verificar na sua conta.
- [ ] **básico** `topic_cowork_projects`: Cowork e Projects no trabalho: projeto com instruções e arquivos, conectores, modos de permissão e tarefas agendadas
  - Entrega: um Project configurado para uma área do seu trabalho e uma tarefa real executada no Cowork.
- [ ] ★ `topic_workflow_trabalho`: Automatizar uma tarefa recorrente do trabalho com processo documentado e medido
  - Entrega: processo em Markdown dentro de `projects/` + medição de tempo antes/depois.
- [ ] ★ `topic_verificacao_saidas`: Verificar saídas de IA: critérios de aceitação, checagem de fatos, testes
  - Evidência: detectar erros plantados numa saída e definir critérios de aceitação antes de pedir.

## Fase 3: Extensões: skills, MCP e hooks (semanas 8–9, ~10 h)

Capacidade observável: diante de uma necessidade, decidir se ela pede instrução (CLAUDE.md/rule), skill, conector/MCP, hook ou permissão, e aplicar o básico de cada um.

- [ ] ★ `topic_skills`: Skills e plugins: quando criar, estrutura de SKILL.md, manutenção e reutilização
  - Transferência natural: criar uma skill para o workflow da Fase 2 (você já mantém a `ai-tutor`). Plugins apenas como conceito: pacote que distribui skills, hooks e servidores MCP juntos.
- [ ] **básico** `topic_integracoes`: MCP e conectores: o que são, como conectar, permissões, riscos e custos
  - Aplicação: conectar um serviço que você já usa (ex.: Google Drive, Gmail, Notion) e executar uma tarefa real com ele, avaliando o que o conector pode acessar.
- [ ] **básico** `topic_hooks_permissoes`: Hooks e regras de permissão: quando usar instrução, hook ou permissão (orientação vs garantia)
  - Ideia central: CLAUDE.md e rules orientam, mas não garantem; hooks e regras de permissão (`allow`/`deny` em `settings.json`) são aplicados pelo cliente.
  - Aplicação: um hook simples ou uma regra `deny` num repositório seu.
- [ ] **opcional** `topic_automacao_python`: Pequenas automações em Python construídas e testadas com Claude Code
  - Entrega: script em `projects/<slug>/` com teste executado e resultado registrado.

## Fase 4: Primeiro serviço com IA (semanas 10–13, ~16 h)

Capacidade observável: uma oferta concreta validada com pessoas reais, não só no papel.

- [ ] ★ `topic_nicho_problema`: Escolher nicho e problema de serviço a partir da própria experiência e de conversas reais
  - Evidência: notas de pelo menos 3 conversas com potenciais clientes.
- [ ] ★ `topic_oferta_servico`: Desenhar a oferta: escopo, entregáveis, preço, riscos, LGPD e responsabilidades
  - Entrega: proposta de uma página.
- [ ] ★ `topic_piloto_cliente`: Executar piloto ou apresentar proposta a um cliente potencial e registrar aprendizados

---

## Fontes verificadas nesta revisão (acesso em 2026-10-01)

- Claude Code Docs: How Claude remembers your project (CLAUDE.md, `.claude/rules/`, auto memory): https://code.claude.com/docs/en/memory
- Claude Code Docs: Extend Claude with skills: https://code.claude.com/docs/en/skills
- Claude Code Docs: Connect Claude Code to tools via MCP: https://code.claude.com/docs/en/mcp
- Claude Code Docs: Automate actions with hooks: https://code.claude.com/docs/en/hooks-guide
- Claude Code Docs: Configure permissions: https://code.claude.com/docs/en/permissions
- Claude Code Docs: Plugins overview: https://code.claude.com/docs/en/plugins/overview
- Claude Code Docs: Desktop application: https://code.claude.com/docs/en/desktop
- Claude Help Center: Get started with Claude Cowork: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- Claude Help Center: Get started with Claude in Chrome: https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome

## Revisões do roadmap

- 2026-10-01 (rev. 2): pedido do aluno para incluir o básico de skills, MCP, hooks e rules e o ecossistema do app (Projects, Cowork, Claude in Chrome). Sem aumentar o orçamento de 52 h:
  - rules incorporadas a `topic_cc_contexto`; ecossistema incorporado a `topic_escolha_ambiente`; plugins incorporados a `topic_skills`;
  - `topic_integracoes` focado em MCP e conectores;
  - novos tópicos básicos: `topic_cowork_projects` e `topic_hooks_permissoes`;
  - Fase 2 ganha uma semana; Fase 3 cai para 2 semanas; `topic_automacao_python` passa a opcional.
  - Nenhuma evidência existia; nenhum histórico foi perdido.
- 2026-10-01 (rev. 1): currículo inicial criado no setup. Nenhuma evidência ou domínio registrado.
