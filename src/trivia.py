from __future__ import annotations

import html
import requests

TRIVIA_API_URL = "https://opentdb.com/api.php"

CATEGORIES = {
    "1": (9, "Conhecimentos Gerais"),
    "2": (17, "Ciência e Natureza"),
    "3": (18, "Computação"),
    "4": (19, "Matemática"),
    "5": (23, "História"),
}


def fetch_question(category_id: int = 9) -> dict:
    params = {
        "amount": 1,
        "category": category_id,
        "type": "multiple",
    }
    response = requests.get(TRIVIA_API_URL, params=params, timeout=5)
    response.raise_for_status()

    data = response.json()

    if data.get("response_code") != 0 or not data.get("results"):
        raise ValueError("A API não retornou perguntas válidas.")

    raw = data["results"][0]

    return {
        "question": html.unescape(raw["question"]),
        "correct_answer": html.unescape(raw["correct_answer"]),
        "incorrect_answers": [html.unescape(a) for a in raw["incorrect_answers"]],
        "category": html.unescape(raw["category"]),
        "difficulty": raw["difficulty"],
    }


def run_quiz() -> None:
    import random

    print("\n--- QUIZ DE ESTUDOS ---")
    print("Escolha uma categoria:")
    for key, (_, name) in CATEGORIES.items():
        print(f"  {key} - {name}")

    choice = input("\nCategoria (1-5): ").strip()
    category_id, category_name = CATEGORIES.get(choice, (9, "Conhecimentos Gerais"))

    print(f"\nBuscando pergunta de '{category_name}'...")

    try:
        q = fetch_question(category_id)
    except Exception as error:
        print(f"Erro ao buscar pergunta: {error}")
        return

    answers = q["incorrect_answers"] + [q["correct_answer"]]
    random.shuffle(answers)

    print(f"\nCategoria : {q['category']}")
    print(f"Dificuldade: {q['difficulty']}")
    print(f"\nPergunta: {q['question']}\n")

    for i, ans in enumerate(answers, start=1):
        print(f"  {i}. {ans}")

    try:
        user_choice = int(input("\nSua resposta (número): "))
        chosen = answers[user_choice - 1]
    except (ValueError, IndexError):
        print("Opção inválida.")
        return

    if chosen == q["correct_answer"]:
        print("✔ Correto! Parabéns.")
    else:
        print(f"✘ Errado. A resposta correta era: {q['correct_answer']}")