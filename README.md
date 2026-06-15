# Organizador de Estudos CLI

> **Repositório:** https://github.com/pedrosallorenzo/organizador_estudos_bc2
> **Deploy:** aplicação CLI — execute localmente seguindo as instruções abaixo.

![CI](https://github.com/pedrosallorenzo/organizador_estudos_bc2/actions/workflows/ci.yml/badge.svg)

---

## 👥 Integrantes do Grupo

| Nome | Matrícula |
|---|---|
| Pedro Sallorenzo | 22505884 |
| Mateus Reis | 22502427 |
| Vinicius Jorge | 22503800 |
| Victor Marques | 22507339 |

---

## Descrição do problema

Muitos estudantes enfrentam dificuldades para manter uma rotina de estudos organizada. Isso pode gerar esquecimentos, acúmulo de atividades, baixa produtividade e dificuldade para acompanhar conteúdos ao longo do tempo.

---

## Proposta da solução

O **Organizador de Estudos CLI** é uma aplicação de linha de comando desenvolvida em Python que permite ao usuário gerenciar tarefas de estudo de forma simples e eficiente, com persistência em banco de dados na nuvem e integração com quiz de conhecimentos.

---

## Público-alvo

- Estudantes do ensino médio
- Estudantes universitários
- Pessoas que desejam organizar melhor a rotina de estudos

---

## Funcionalidades

- Adicionar nova tarefa
- Listar tarefas
- Concluir tarefa
- Remover tarefa
- Filtrar tarefas por status (pendente, concluída ou todas)
- Quiz de estudos com perguntas de múltipla escolha por categoria
- Persistência de dados no Supabase (PostgreSQL em nuvem)

---

## Tecnologias utilizadas

- Python 3.12
- Supabase (PostgreSQL em nuvem)
- Requests
- Pytest
- Ruff
- GitHub Actions (CI/CD)
- python-dotenv

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
│   ├── test_filter.py
│   ├── test_storage.py
│   ├── test_task_manager.py
│   └── test_trivia.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

---

## Como executar localmente

### Pré-requisitos

- Python 3.12 ou superior
- `uv` instalado ([instruções](https://docs.astral.sh/uv/getting-started/installation/))
- Conta no [Supabase](https://supabase.com) com projeto e tabela `tasks` configurados

### Configuração do ambiente

```bash
# 1. Clone o repositório
git clone https://github.com/pedrosallorenzo/organizador_estudos_bc2.git
cd organizador_estudos_bc2

# 2. Crie o arquivo .env com suas credenciais
cp .env.example .env
# Edite o .env com sua SUPABASE_URL e SUPABASE_KEY

# 3. Crie o ambiente virtual e instale as dependências
uv venv
uv pip install -r requirements.txt

# 4. Execute a aplicação
PYTHONPATH=src uv run python src/main.py
```

### Configuração do Supabase

Crie uma tabela `tasks` no seu projeto Supabase com as colunas:

| Coluna | Tipo | Padrão |
|---|---|---|
| id | int8 | auto |
| title | text | — |
| done | bool | false |

### Menu da aplicação

```
ORGANIZADOR DE ESTUDOS CLI
1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover tarefa
5 - Filtrar tarefas por status
6 - Quiz de estudos
7 - Sair
```

---

## Como rodar os testes

```bash
PYTHONPATH=. uv run pytest
```

---

## CI/CD

O projeto utiliza **GitHub Actions** para validação contínua a cada push e pull request:

1. Lint com **Ruff**
2. Testes unitários e de integração com **Pytest**

Status atual: ![CI](https://github.com/pedrosallorenzo/organizador_estudos_bc2/actions/workflows/ci.yml/badge.svg)
