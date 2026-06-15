import pytest
from src.task_manager import TaskManager

TASKS = [
    {"title": "Estudar Python", "done": False},
    {"title": "Revisar lógica", "done": True},
    {"title": "Fazer resumo", "done": False},
    {"title": "Ler documentação", "done": True},
]


def test_filter_pendente() -> None:
    manager = TaskManager(list(TASKS))
    result = manager.filter_tasks("pendente")
    assert len(result) == 2
    assert all(not t["done"] for t in result)


def test_filter_concluida() -> None:
    manager = TaskManager(list(TASKS))
    result = manager.filter_tasks("concluida")
    assert len(result) == 2
    assert all(t["done"] for t in result)


def test_filter_todas() -> None:
    manager = TaskManager(list(TASKS))
    result = manager.filter_tasks("todas")
    assert len(result) == 4


def test_filter_status_invalido() -> None:
    manager = TaskManager(list(TASKS))
    with pytest.raises(ValueError, match="Status inválido"):
        manager.filter_tasks("errado")


def test_filter_lista_vazia() -> None:
    manager = TaskManager([])
    assert manager.filter_tasks("pendente") == []
    assert manager.filter_tasks("concluida") == []