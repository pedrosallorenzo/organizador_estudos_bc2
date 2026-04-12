from __future__ import annotations

# Gerencia as tarefas de estudo
class TaskManager:

    def __init__(self, tasks: list[dict] | None = None) -> None:
        self.tasks = tasks if tasks is not None else []

    # Adicionar uma nova tarefa
    def add_task(self, title: str) -> dict:
        normalized_title = title.strip()

        if not normalized_title:
            raise ValueError("O título da tarefa não pode ser vazio.")

        task = {
            "title": normalized_title,
            "done": False,
        }
        self.tasks.append(task)
        return task

    # Retorna a lista de tarefas
    def list_tasks(self) -> list[dict]:
        return self.tasks

    # Marca como concluída a tarefa
    def complete_task(self, index: int) -> dict:
        self._validate_index(index)
        self.tasks[index]["done"] = True
        return self.tasks[index]

    # Removo e retorna a tarefa
    def remove_task(self, index: int) -> dict:
        self._validate_index(index)
        return self.tasks.pop(index)

    # Valida se o índice existe
    def _validate_index(self, index: int) -> None:
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Índice de tarefa inválido.")