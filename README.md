# Organizador de Estudos CLI

> **Repositório:** https://github.com/pedrosallorenzo/organizador_estudos_bc2  
> **Autor:** Pedro Henrique Silva Sallorenzo  
> **Deploy:** aplicação CLI — execute localmente seguindo as instruções abaixo.

![CI](https://github.com/pedrosallorenzo/organizador_estudos_bc2/actions/workflows/ci.yml/badge.svg)

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
- salvar as tarefas localmente em arquivo JSON;
- realizar um **quiz de estudos** integrado com a Open Trivia DB.

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
- persistir dados em arquivo JSON;
- **quiz de estudos** com perguntas de múltipla escolha por categoria (Conhecimentos Gerais, Ciência, Computação, Matemática e História), consumindo a [Open Trivia DB](https://opentdb.com/).

---

## Integração com API Pública

A aplicação consome a **Open Trivia DB** (`https://opentdb.com/api.php`), uma API gratuita e aberta que fornece perguntas de quiz por categoria e dificuldade. Nenhuma chave de API é necessária.

A requisição é feita via HTTP GET e os dados retornados são exibidos diretamente no terminal, permitindo ao usuário responder perguntas relacionadas às matérias que está estudando.

---

## Tecnologias utilizadas

- Python 3.12
- Requests
- Pytest
- Ruff
- GitHub Actions (CI)
- JSON para armazenamento local

---

## Estrutura do projeto

```
organizador-estudos/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── storage.py
│   ├── task_manager.py
│   └── trivia.py
├── tests/
│   ├── test_task_manager.py
│   └── test_trivia.py
├── data/
│   └── tasks.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── requirements.txt
├── uv.lock
└── VERSION
```

---

## Como executar localmente (Deploy CLI)

### Pré-requisitos

- Python 3.12 ou superior instalado
- `uv` instalado ([instruções](https://docs.astral.sh/uv/getting-started/installation/))

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/pedrosallorenzo/organizador_estudos_bc2.git
cd organizador_estudos_bc2

# 2. Crie o ambiente virtual e instale as dependências
uv venv
uv pip install -r requirements.txt

# 3. Execute a aplicação
PYTHONPATH=src uv run python src/main.py
```

### Menu da aplicação

```
ORGANIZADOR DE ESTUDOS CLI
1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover tarefa
5 - Quiz de estudos
6 - Sair
```

---

## Como rodar os testes

```bash
PYTHONPATH=. uv run pytest
```

---

## CI/CD

O projeto utiliza **GitHub Actions** para validação contínua a cada push e pull request. O pipeline executa:

1. Lint com **Ruff**
2. Testes unitários e de integração com **Pytest**

Status atual: ![CI](https://github.com/pedrosallorenzo/organizador_estudos_bc2/actions/workflows/ci.yml/badge.svg)