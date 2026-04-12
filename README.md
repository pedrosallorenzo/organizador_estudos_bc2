# Organizador de Estudos CLI

Aplicação simples em Python com interface de linha de comando (CLI) para ajudar estudantes a organizarem suas tarefas de estudo de forma prática, rápida e acessível.

---

## Descrição do problema

Muitos estudantes enfrentam dificuldades para manter uma rotina de estudos organizada. Isso pode gerar esquecimentos, acúmulo de atividades, baixa produtividade e dificuldade para acompanhar conteúdos ao longo do tempo.

---

## Proposta da solução

O **Organizador de Estudos CLI** foi desenvolvido para amenizar esse problema por meio de uma aplicação simples de terminal, permitindo ao usuário:

- cadastrar tarefas de estudo;
- listar tarefas cadastradas;
- marcar tarefas como concluídas;
- remover tarefas;
- salvar as tarefas localmente em arquivo JSON.

A proposta é oferecer uma solução leve e funcional, com baixo nível de complexidade, mas com organização técnica, testes automatizados e validação contínua.

---

## Público-alvo

- estudantes do ensino médio;
- estudantes universitários;
- pessoas que desejam organizar melhor a rotina de estudos.

---

## Funcionalidades principais

- adicionar nova tarefa;
- listar tarefas;
- concluir tarefa;
- remover tarefa;
- persistir dados em arquivo JSON.

---

## Tecnologias utilizadas

- Python 3
- Pytest
- Ruff
- GitHub Actions
- JSON para armazenamento local

---

## Estrutura do projeto

``` id="9x5l0b"
organizador-estudos/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── storage.py
│   └── task_manager.py
├── tests/
│   └── test_task_manager.py
├── data/
│   └── tasks.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml
├── README.md
├── uv.lock
└── VERSION