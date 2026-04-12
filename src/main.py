from __future__ import annotations

from storage import load_tasks, save_tasks
from task_manager import TaskManager

DATA_FILE = "data/tasks.json"


def show_menu() -> None:
    print("\nORGANIZADOR DE ESTUDOS CLI")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")


def print_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\nLista de tarefas:")
    for i, task in enumerate(tasks, start=1):
        status = "Concluída" if task["done"] else "Pendente"
        print(f"{i}. {task['title']} [{status}]")


def add_task_flow(manager: TaskManager) -> None:
    title = input("\nDigite o título da tarefa: ")

    try:
        manager.add_task(title)
        save_tasks(DATA_FILE, manager.list_tasks())
        print("Tarefa adicionada com sucesso.")
    except ValueError as error:
        print(f"Erro: {error}")


def complete_task_flow(manager: TaskManager) -> None:
    tasks = manager.list_tasks()
    print_tasks(tasks)

    if not tasks:
        return

    try:
        choice = int(input("\nDigite o número da tarefa a concluir: "))
        manager.complete_task(choice - 1)
        save_tasks(DATA_FILE, manager.list_tasks())
        print("Tarefa concluída com sucesso.")
    except ValueError:
        print("Erro: digite um número válido.")
    except IndexError as error:
        print(f"Erro: {error}")


def remove_task_flow(manager: TaskManager) -> None:
    tasks = manager.list_tasks()
    print_tasks(tasks)

    if not tasks:
        return

    try:
        choice = int(input("\nDigite o número da tarefa a remover: "))
        removed_task = manager.remove_task(choice - 1)
        save_tasks(DATA_FILE, manager.list_tasks())
        print(f"Tarefa removida com sucesso: {removed_task['title']}")
    except ValueError:
        print("Erro: digite um número válido.")
    except IndexError as error:
        print(f"Erro: {error}")


def main() -> None:
    tasks = load_tasks(DATA_FILE)
    manager = TaskManager(tasks)

    while True:
        show_menu()
        option = input("\nEscolha uma opção: ").strip()

        if option == "1":
            add_task_flow(manager)
        elif option == "2":
            print_tasks(manager.list_tasks())
        elif option == "3":
            complete_task_flow(manager)
        elif option == "4":
            remove_task_flow(manager)
        elif option == "5":
            print("\nEncerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()