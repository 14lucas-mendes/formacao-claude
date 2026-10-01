# Currículo: Claude Code aplicado ao trabalho e a serviços com IA

<!-- Itens são adicionados pelo workflow de currículo com IDs estáveis. -->

**Objetivo (até 2026-12-31):** (1) usar Claude Code e Cowork no fluxo de trabalho diário de forma segura, verificável e documentada; (2) ter uma primeira oferta de serviço com IA definida, com piloto entregue ou proposta apresentada a pelo menos um cliente potencial.

**Fora do escopo:** construir produto/SaaS próprio.

**Orçamento de tempo:** 4 h/semana × ~13 semanas ≈ 52 h, em sessões de ~1 h, preferencialmente no fim de semana.

**Regra de conclusão:** um item só é marcado quando o tópico atinge domínio 80 (explicação Feynman autônoma + aplicação autônoma + aplicação transferida para novo contexto), com IDs de evidência registrados no `session-log.md`. Ler conteúdo ou receber explicação não conta como evidência.

**Prioridade realista:** com 52 h, os itens marcados com ★ são o núcleo e devem chegar a 80. Os demais podem fechar o prazo em 60 sem comprometer o objetivo.

**Fontes primárias:** documentação oficial do Claude Code (https://code.claude.com/docs) e da Anthropic (https://docs.claude.com). As fontes específicas são registradas por lição via `/sources`.

---

## Fase 1: Fundamentos operacionais (semanas 1–3, ~12 h)

Capacidade observável: conduzir uma tarefa real no Claude Code sabendo o que ele está fazendo, por que, e como desfazer.

- [ ] ★ `topic_cc_modelo_mental`: Modelo mental do Claude Code: loop agêntico, ferramentas, contexto e limites
  - Evidências: Feynman (explicar o ciclo pedido → plano → ferramentas → verificação); aplicação (conduzir uma tarefa e narrar as decisões do agente); transferência (prever o comportamento numa tarefa diferente).
- [ ] ★ `topic_cc_contexto`: Gestão de contexto: CLAUDE.md, sessões, /clear e /compact, documentação vs memória
  - Entrega: um `CLAUDE.md` útil escrito por você para um repositório real seu.
- [ ] ★ `topic_cc_seguranca`: Trabalho seguro: modos de permissão, revisão de diffs, Git como rede de segurança, dados sensíveis
  - Entrega: checklist pessoal de segurança aplicado a uma tarefa real, com um commit revisado por você.

## Fase 2: Fluxo de trabalho diário (semanas 4–6, ~12 h)

Capacidade observável: uma tarefa recorrente do seu trabalho passa a ser feita com IA, com tempo medido antes e depois.

- [ ] ★ `topic_escolha_ambiente`: Escolher o ambiente certo: Chat, Projects, Cowork, Claude Code local e na nuvem
  - Evidência: para 3 tarefas reais, escolher o ambiente e justificar; transferência com uma tarefa nova.
- [ ] ★ `topic_workflow_trabalho`: Automatizar uma tarefa recorrente do trabalho com processo documentado e medido
  - Entrega: processo em Markdown dentro de `projects/` + medição de tempo antes/depois.
- [ ] ★ `topic_verificacao_saidas`: Verificar saídas de IA: critérios de aceitação, checagem de fatos, testes
  - Evidência: detectar erros plantados numa saída e definir critérios de aceitação antes de pedir.

## Fase 3: Reutilização e integração (semanas 7–9, ~12 h)

Capacidade observável: transformar o que funciona em algo reutilizável, sem complexidade desnecessária.

- [ ] ★ `topic_skills`: Skills: quando criar, estrutura de SKILL.md, manutenção e reutilização
  - Transferência natural: criar uma skill para o workflow da Fase 2 (você já mantém a `ai-tutor`).
- [ ] `topic_integracoes`: Integrações: conectores/MCP, hooks e automações recorrentes, com riscos e custos
- [ ] `topic_automacao_python`: Pequenas automações em Python construídas e testadas com Claude Code
  - Entrega: script em `projects/<slug>/` com teste executado e resultado registrado.

## Fase 4: Primeiro serviço com IA (semanas 10–13, ~16 h)

Capacidade observável: uma oferta concreta validada com pessoas reais, não só no papel.

- [ ] ★ `topic_nicho_problema`: Escolher nicho e problema de serviço a partir da própria experiência e de conversas reais
  - Evidência: notas de pelo menos 3 conversas com potenciais clientes.
- [ ] ★ `topic_oferta_servico`: Desenhar a oferta: escopo, entregáveis, preço, riscos, LGPD e responsabilidades
  - Entrega: proposta de uma página.
- [ ] ★ `topic_piloto_cliente`: Executar piloto ou apresentar proposta a um cliente potencial e registrar aprendizados

---

## Revisões do roadmap

- 2026-10-01: currículo inicial criado no setup. Nenhuma evidência ou domínio registrado.
