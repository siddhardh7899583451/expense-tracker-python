from unittest.mock import patch
from datetime import datetime
from expense_tracker.validators import (
    get_valid_title,
    get_valid_amount,
    get_valid_category,
    get_valid_date,
)


def test_get_valid_title():
    # Simulate entering an empty string first, then 'Groceries'
    with patch("builtins.input", side_effect=["", "  ", "Groceries"]):
        assert get_valid_title() == "Groceries"


def test_get_valid_amount_invalid_then_valid():
    # Simulate entering invalid 'abc', negative '-10', zero '0', then valid '120.5'
    with patch("builtins.input", side_effect=["abc", "-10", "0", "120.5"]):
        assert get_valid_amount() == 120.5


def test_get_valid_category():
    # Simulate empty input first, then 'Food'
    with patch("builtins.input", side_effect=["", "Food"]):
        assert get_valid_category() == "Food"


def test_get_valid_date_blank():
    # Simulate leaving input blank (should return today's date in YYYY-MM-DD format)
    with patch("builtins.input", return_value=""):
        expected_today = datetime.today().strftime("%Y-%m-%d")
        assert get_valid_date() == expected_today


def test_get_valid_date_custom_valid():
    with patch("builtins.input", return_value="2026-07-25"):
        assert get_valid_date() == "2026-07-25"


def test_get_valid_date_invalid_then_valid():
    # Simulate bad date format, invalid month/day, then valid date
    with patch(
        "builtins.input", side_effect=["25-07-2026", "2026-15-99", "2026-07-25"]
    ):
        assert get_valid_date() == "2026-07-25"


def test_get_valid_amount_integer():
    with patch("builtins.input", return_value="250"):
        assert get_valid_amount() == 250.0
