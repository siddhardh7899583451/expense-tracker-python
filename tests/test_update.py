from expense_tracker.manager import ExpenseManager
from expense_tracker.storage import CSVStorage


def test_update_expense_success(tmp_path):
    storage = CSVStorage(tmp_path / "expenses.csv")
    manager = ExpenseManager(storage=storage)

    manager.add_expense(
        "Coffee",
        120,
        "Food",
        "2026-07-25",
    )

    result = manager.update_expense(
        0,
        "Tea",
        50,
        "Food",
        "2026-07-26",
    )

    assert result is True

    expenses = manager.get_all_expenses()

    assert expenses[0].title == "Tea"
    assert expenses[0].amount == 50


def test_update_invalid_expense(tmp_path):
    storage = CSVStorage(tmp_path / "expenses.csv")
    manager = ExpenseManager(storage=storage)

    assert (
        manager.update_expense(
            5,
            "Test",
            100,
            "Food",
            "2026-07-26",
        )
        is False
    )