from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

def _make_supabase_client(rows: list[dict] | None = None) -> MagicMock:
    # Monta um mock do cliente Supabase.
    mock_client = MagicMock()

    # Mock para SELECT
    mock_select = MagicMock()
    mock_select.execute.return_value = MagicMock(data=rows or [])
    mock_client.table.return_value.select.return_value = mock_select

    # Mock para DELETE
    mock_delete = MagicMock()
    mock_delete.execute.return_value = MagicMock(data=[])
    mock_client.table.return_value.delete.return_value.neq.return_value = mock_delete

    # Mock para INSERT
    mock_insert = MagicMock()
    mock_insert.execute.return_value = MagicMock(data=[])
    mock_client.table.return_value.insert.return_value = mock_insert

    return mock_client

class TestLoadTasks:
    def test_retorna_lista_de_tarefas(self) -> None:
        # load_tasks deve retornar a lista de tarefas do Supabase
        rows = [
            {"id": 1, "title": "Estudar Python", "done": False},
            {"id": 2, "title": "Revisar lógica", "done": True},
        ]
        mock_client = _make_supabase_client(rows)

        with patch("src.storage.get_client", return_value=mock_client):
            from src.storage import load_tasks
            result = load_tasks()

        assert len(result) == 2
        assert result[0]["title"] == "Estudar Python"
        assert result[1]["done"] is True

    def test_retorna_lista_vazia_quando_banco_vazio(self) -> None:
        # load_tasks deve retornar [] quando não há tarefas no banco
        mock_client = _make_supabase_client([])

        with patch("src.storage.get_client", return_value=mock_client):
            from src.storage import load_tasks
            result = load_tasks()

        assert result == []


class TestSaveTasks:
    def test_salva_tarefas_no_supabase(self) -> None:
        # save_tasks deve deletar e re-inserir as tarefas
        tasks = [
            {"title": "Estudar Python", "done": False},
            {"title": "Fazer resumo", "done": True},
        ]
        mock_client = _make_supabase_client()

        with patch("src.storage.get_client", return_value=mock_client):
            from src.storage import save_tasks
            save_tasks("", tasks)

        # Verifica que delete e insert foram chamados
        mock_client.table.return_value.delete.assert_called()
        mock_client.table.return_value.insert.assert_called()

    def test_nao_insere_quando_lista_vazia(self) -> None:
        # save_tasks não deve chamar insert quando a lista está vazia
        mock_client = _make_supabase_client()

        with patch("src.storage.get_client", return_value=mock_client):
            from src.storage import save_tasks
            save_tasks("", [])

        mock_client.table.return_value.insert.assert_not_called()