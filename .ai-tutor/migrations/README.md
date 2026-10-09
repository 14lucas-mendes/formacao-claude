# Registros históricos de migração

Os arquivos desta pasta documentam o estado e as decisões no momento de cada migração. São snapshots históricos, não fontes da configuração atual. Preserve-os mesmo quando novas revisões alterarem as trilhas.

A única fonte vigente de `curriculum_tracks` é `.ai-tutor/study-config.json`. O tutor usa essa configuração para selecionar o núcleo e reportar progresso; `scripts/validate_curriculum.py` verifica sua consistência com o estado e o checklist. Nenhum desses fluxos deve buscar a classificação atual nos snapshots.
