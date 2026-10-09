#!/usr/bin/env python3
"""Valide as trilhas ativas do estudo sem modificar a skill ou o histórico."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re


TRACKS = ("core_topic_ids", "optional_topic_ids", "retired_topic_ids")
TOPIC_ID = re.compile(r"topic_[A-Za-z0-9_-]+")
CHECKLIST = re.compile(r"^- \[[ xX]\] `(topic_[A-Za-z0-9_-]+)`:", re.MULTILINE)


def validate_curriculum(study_root: Path) -> list[str]:
    """Retorne erros da classificação vigente; migrações são snapshots históricos."""
    root = study_root.resolve()
    payloads = {}
    errors = []
    for relative in (".ai-tutor/study-config.json", ".ai-tutor/state.json", "curriculum.md"):
        try:
            text = (root / relative).read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            errors.append(f"não foi possível ler {relative}: {exc}")
            continue
        if relative.endswith(".json"):
            try:
                payloads[relative] = json.loads(text)
            except json.JSONDecodeError as exc:
                errors.append(f"JSON inválido em {relative}: {exc}")
        else:
            payloads[relative] = text
    if errors:
        return errors

    config = payloads[".ai-tutor/study-config.json"]
    state = payloads[".ai-tutor/state.json"]
    if not isinstance(config, dict) or not isinstance(state, dict):
        return ["configuração e estado devem ser objetos JSON"]
    tracks = config.get("curriculum_tracks")
    topics = state.get("topics")
    if not isinstance(tracks, dict):
        return ["curriculum_tracks deve ser um objeto na configuração ativa"]
    if not isinstance(topics, list):
        return ["topics deve ser uma lista no estado"]

    state_ids = []
    for position, topic in enumerate(topics):
        topic_id = topic.get("topic_id") if isinstance(topic, dict) else None
        if not isinstance(topic_id, str) or not TOPIC_ID.fullmatch(topic_id):
            errors.append(f"ID inválido em topics[{position}]")
        else:
            state_ids.append(topic_id)
    for topic_id, count in Counter(state_ids).items():
        if count > 1:
            errors.append(f"ID repetido no estado: {topic_id}")

    classified_ids = []
    for track in TRACKS:
        values = tracks.get(track)
        if not isinstance(values, list):
            errors.append(f"{track} deve ser uma lista")
            continue
        if track == "core_topic_ids" and not values:
            errors.append("core_topic_ids não pode ser vazia")
        valid_ids = []
        for position, topic_id in enumerate(values):
            if not isinstance(topic_id, str) or not TOPIC_ID.fullmatch(topic_id):
                errors.append(f"ID inválido em {track}[{position}]")
            else:
                valid_ids.append(topic_id)
        for topic_id, count in Counter(valid_ids).items():
            if count > 1:
                errors.append(f"ID repetido em {track}: {topic_id}")
        classified_ids.extend(valid_ids)

    if errors:
        return errors
    for topic_id in sorted(set(classified_ids)):
        memberships = sum(topic_id in tracks[track] for track in TRACKS)
        if memberships > 1:
            errors.append(f"ID em mais de uma trilha: {topic_id}")
    for topic_id in sorted(set(state_ids) - set(classified_ids)):
        errors.append(f"tópico sem classificação: {topic_id}")
    for topic_id in sorted(set(classified_ids) - set(state_ids)):
        errors.append(f"tópico classificado ausente do estado: {topic_id}")

    checklist = CHECKLIST.findall(payloads["curriculum.md"])
    if checklist != tracks["core_topic_ids"]:
        errors.append(
            "checklist obrigatório de curriculum.md não corresponde aos core_topic_ids "
            "(IDs e ordem); não inclua opcionais ou históricos no checklist"
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "study_root",
        type=Path,
        nargs="?",
        default=Path(__file__).resolve().parents[1],
        help="raiz do estudo; por padrão, a raiz deste repositório",
    )
    errors = validate_curriculum(parser.parse_args().study_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("CURRICULUM VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
