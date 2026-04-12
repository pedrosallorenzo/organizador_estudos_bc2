from __future__ import annotations

import json
from pathlib import Path

# Garante que o diretório e o arquivo de dados existam
def ensure_data_file(file_path: str) -> Path:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.write_text("[]", encoding="utf-8")

    return path

# Carregar as tarefas em um arquivo .json
# Caso esteja vazio ou inválido, a função
# retorna uma lista vazia
def load_tasks(file_path: str) -> list[dict]: 
    path = ensure_data_file(file_path)

    try:
        content = path.read_text(encoding="utf-8").strip()
        if not content:
            return []

        data = json.loads(content)

        if isinstance(data, list):
            return data

        return []
    except (json.JSONDecodeError, OSError):
        return []

# Salva as tarefas em formato .json
def save_tasks(file_path: str, tasks: list[dict]) -> None:
    path = ensure_data_file(file_path)
    path.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )