from __future__ import annotations

import pytest

from src.task_manager import TaskManager


def test_add_task_success() -> None:
    manager = TaskManager()

    task = manager.add_task("Estudar Python")

    assert len(manager.list_tasks()) == 1
    assert task["title"] == "Estudar Python"
    assert task["done"] is False


def test_add_empty_task_raises_value_error() -> None:
    manager = TaskManager()

    with pytest.raises(ValueError, match="não pode ser vazio"):
        manager.add_task("   ")


def test_complete_task_success() -> None:
    manager = TaskManager([{"title": "Revisar lógica", "done": False}])

    task = manager.complete_task(0)

    assert task["done"] is True
    assert manager.list_tasks()[0]["done"] is True


def test_complete_task_invalid_index_raises_index_error() -> None:
    manager = TaskManager()

    with pytest.raises(IndexError, match="Índice de tarefa inválido"):
        manager.complete_task(0)


def test_remove_task_success() -> None:
    manager = TaskManager(
        [
            {"title": "Estudar matemática", "done": False},
            {"title": "Fazer resumo", "done": False},
        ]
    )

    removed = manager.remove_task(0)

    assert removed["title"] == "Estudar matemática"
    assert len(manager.list_tasks()) == 1
    assert manager.list_tasks()[0]["title"] == "Fazer resumo"