from __future__ import annotations

import pytest
from unittest.mock import patch, MagicMock
from src.trivia import fetch_question, TRIVIA_API_URL


# helpers

def _make_api_response(
    response_code: int = 0,
    question: str = "What is 2 + 2?",
    correct: str = "4",
    incorrect: list[str] | None = None,
) -> MagicMock:
    if incorrect is None:
        incorrect = ["3", "5", "6"]

    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "response_code": response_code,
        "results": [
            {
                "question": question,
                "correct_answer": correct,
                "incorrect_answers": incorrect,
                "category": "Mathematics",
                "difficulty": "easy",
            }
        ]
        if response_code == 0
        else [],
    }
    return mock_response


# Testes de integração

class TestFetchQuestion:

    def test_retorna_estrutura_correta(self) -> None:
        with patch("src.trivia.requests.get", return_value=_make_api_response()) as mock_get:
            result = fetch_question(category_id=19)

        mock_get.assert_called_once_with(
            TRIVIA_API_URL,
            params={"amount": 1, "category": 19, "type": "multiple"},
            timeout=5,
        )
        assert result["question"] == "What is 2 + 2?"
        assert result["correct_answer"] == "4"
        assert len(result["incorrect_answers"]) == 3
        assert result["category"] == "Mathematics"
        assert result["difficulty"] == "easy"

    def test_decodifica_entidades_html(self) -> None:
        with patch(
            "src.trivia.requests.get",
            return_value=_make_api_response(
                question="Who wrote &quot;Hamlet&quot;?",
                correct="William Shakespeare",
                incorrect=["Charles Dickens", "Jane Austen", "Mark Twain"],
            ),
        ):
            result = fetch_question()

        assert result["question"] == 'Who wrote "Hamlet"?'

    def test_levanta_value_error_se_response_code_invalido(self) -> None:
        with patch(
            "src.trivia.requests.get",
            return_value=_make_api_response(response_code=1),
        ):
            with pytest.raises(ValueError, match="não retornou perguntas válidas"):
                fetch_question()

    def test_levanta_excecao_em_falha_de_rede(self) -> None:
        import requests as req

        with patch("src.trivia.requests.get", side_effect=req.RequestException("timeout")):
            with pytest.raises(req.RequestException):
                fetch_question()