# Instruções para o Claude

Este repositório é um programa de estudos conduzido pela skill `ai-tutor`.

- `skill_root`: `.claude/skills/ai-tutor/` (somente leitura; é uma cópia do repositório `ai-tutor-skill`).
- `study_root`: a raiz deste repositório.
- Ao retomar estudos, siga `references/workflows/session.md` da skill.
- Validar o estado após cada mudança, executando a partir de `skill_root`:
  `python3 -m scripts.validate_study <caminho absoluto da raiz do repo>`.
  O comando documentado `python scripts/validate_study.py` falha com `ModuleNotFoundError` nesta versão da skill.
- Responder em português brasileiro.
