# Formação profissional em Claude Code

Formação prática para conduzir trabalho de desenvolvimento com Claude Code: entender um repositório, especificar uma mudança, implementar, depurar, testar, revisar e entregar uma PR com evidências. O foco é dominar o ambiente de programação agêntica e supervisionar suas decisões.

**Carga prevista:** 26 semanas × 4 h/semana = 104 h, em sessões de cerca de 1 h. O calendário existente termina em **2027-03-31**, com uma revisão de uso diário em **2026-12-31**. A carga é uma estimativa; a conclusão depende de competência demonstrada.

A manutenção industrial continua como contexto dos exemplos. Python é a linguagem dos laboratórios, e o método também se aplica a outros projetos. Claude Chat, Cowork, criação de agentes via API e venda de serviços deixam de ser requisitos da formação.

## Resultado esperado

Ao concluir, você será capaz de:

- Preparar Claude Code no terminal e usar a integração com seu editor.
- Organizar contexto, instruções, permissões, sessões e consumo.
- Conduzir mudanças em código existente com critérios de aceitação e testes.
- Investigar bugs, revisar diffs, trabalhar com branches e entregar PRs.
- Criar e verificar skills, hooks, integrações MCP e subagentes.
- Usar worktrees, execução não interativa e CI com escopo e acesso controlados.
- Demonstrar um projeto reproduzível, explicar decisões e resolver uma tarefa nova.

## Comece aqui

1. Tenha Git, Python **3.11+** e acesso autorizado ao Claude Code. Use a [instalação oficial](https://code.claude.com/docs/en/setup) para seu sistema. Confira autenticação, plano e cobrança na sua conta; o estudo não exige contratar uma API separada.
2. Clone este repositório e abra o terminal na pasta dele.
3. Verifique a instalação e abra o tutor:

   ```sh
   claude --version
   claude doctor
   claude
   ```

4. Dentro da sessão, envie `/ai-tutor continue meus estudos`. O tutor deve retomar a sessão interrompida antes de avançar.
5. Consulte o [currículo](curriculum.md), o [guia de trabalho](docs/guia-profissional.md) e os [laboratórios](docs/laboratorios/README.md).

Outros pedidos dentro da sessão: `/ai-tutor /licao`, `/ai-tutor /review`, `/ai-tutor /progress` e `/ai-tutor /sources`. São intenções interpretadas pela skill deste projeto.

## Como estudar e comprovar domínio

Cada sessão combina explicação curta, prática com Claude Code, tentativa autônoma do aluno e revisão. O código pode ser produzido em colaboração com o agente; explicar, avaliar e transferir o método a uma tarefa nova são responsabilidades do aluno.

Um tópico obrigatório só é concluído em **domínio 80**, com explicação autônoma, aplicação autônoma e aplicação em outro contexto. Conteúdo recebido, código gerado e tempo de estudo não comprovam domínio. Registre arquivos, comandos, resultados e IDs de evidência com o tutor. Os enunciados dos laboratórios são material de estudo, não entregas já concluídas.

As trilhas vigentes estão somente em `.ai-tutor/study-config.json`; a migração guarda um snapshot histórico. Em `/progress` e `/review`, o tutor considera o núcleo obrigatório e apresenta opcionais e históricos à parte. Essa adaptação é definida pelas instruções do projeto em `CLAUDE.md`; a skill vendorizada não interpreta `curriculum_tracks` nativamente.

## Estrutura

| Caminho | Uso |
| --- | --- |
| [curriculum.md](curriculum.md) | Fases, competências, pré-requisitos e critérios |
| [docs/guia-profissional.md](docs/guia-profissional.md) | Método de trabalho, comandos e revisão |
| [docs/laboratorios/](docs/laboratorios/README.md) | Oito laboratórios e projeto integrador |
| [docs/templates/entrega.md](docs/templates/entrega.md) | Modelo de registro de tarefa, retomada e PR |
| [docs/fontes.md](docs/fontes.md) | Referências oficiais e política de atualização |
| [docs/proposta-formacao-claude-code.md](docs/proposta-formacao-claude-code.md) | Diagnóstico do projeto e justificativa da mudança |
| `session-log.md` / `flashcards.md` | Sessões e revisão espaçada |
| `lessons/` | Lições adaptadas e registradas pelo tutor |
| `projects/` | Trabalhos do aluno e dados fictícios para prática |
| `.ai-tutor/` | Configuração e estado canônico em JSON |
| `.claude/skills/ai-tutor/` | Cópia da skill de acompanhamento |
| [scripts/validate_curriculum.py](scripts/validate_curriculum.py) | Verificação das trilhas e do checklist obrigatório |
| [.github/workflows/validate-study.yml](.github/workflows/validate-study.yml) | Testes e validadores em pushes e PRs |

## Validar o estudo

A partir da raiz do repositório, em um shell POSIX ou PowerShell:

```sh
python3 scripts/validate_curriculum.py
python3 -m unittest discover -s tests -v
cd .claude/skills/ai-tutor
python3 -m scripts.validate_study ../../..
```

Se o seu sistema usa `python` para Python 3.11+, substitua `python3`. Execute como módulo: nesta versão, chamar `scripts/validate_study.py` diretamente falha no import.

O validador curricular rejeita IDs sem classificação, repetidos, presentes em mais de uma trilha ou ausentes do estado, além de divergências entre o núcleo e o checklist. Ele usa apenas a configuração vigente; snapshots de migração não precisam acompanhar revisões futuras. Essa checagem não substitui a validação de evidências e sessões feita pela skill.

O CI executa esses testes e validadores com Python 3.11, sem depender de Claude Code, MCP ou credenciais de API. O pipeline verifica arquivos e invariantes; não comprova o comportamento pedagógico do tutor nem realiza os exercícios do aluno.

Não reinicialize o estudo para aplicar a nova trilha: o ID do estudo, as evidências e os checkpoints devem continuar preservados.

## Tutor e atualizações

A formação usa a skill [ai-tutor](https://github.com/14lucas-mendes/ai-tutor-skill), instalada para funcionar também em sessões na nuvem. Origem da cópia: commit `db41bf3`. Seu código é tratado como somente leitura neste projeto; as regras específicas da formação ficam em `CLAUDE.md`, no currículo e na configuração do estudo.

A cópia não se atualiza sozinha. Em uma atualização dedicada, revise a origem, substitua o pacote e atualize o commit documentado. A cópia atual não inclui `agents/openai.yaml`, exigido por seu validador de pacote; isso já ocorria antes desta revisão. O validador do estado de estudo funciona.

Recursos do Claude Code mudam. Registre versão, sistema e fonte em cada laboratório; confira `claude --help` e a documentação antes de usar opções novas.
