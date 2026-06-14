from __future__ import annotations

import os

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")


def get_client() -> Client:
    # Retorna um cliente Supabase autenticado.
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise EnvironmentError(
            "Variáveis de ambiente SUPABASE_URL e SUPABASE_KEY não configuradas."
        )
    return create_client(SUPABASE_URL, SUPABASE_KEY)


def load_tasks(_file_path: str = "") -> list[dict]:
    # Carrega todas as tarefas do Supabase
    client = get_client()
    response = client.table("tasks").select("*").execute()
    return [
        {"id": row["id"], "title": row["title"], "done": row["done"]}
        for row in response.data
    ]


def save_tasks(_file_path: str, tasks: list[dict]) -> None:
    # Sincroniza a lista de tarefas com o Supabase
    client = get_client()
    client.table("tasks").delete().neq("id", 0).execute()
    if tasks:
        rows = [{"title": t["title"], "done": t["done"]} for t in tasks]
        client.table("tasks").insert(rows).execute()