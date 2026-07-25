from expense_tracker.manager import ExpenseManager
from expense_tracker.storage import CSVStorage


def test_delete_expense_success(tmp_path):
    manager = ExpenseManager()
    # Pass the custom temp file path into CSVStorage on initialization
    # so __init__ writes the CSV header properly!
    manager.storage = CSVStorage(tmp_path / "expenses.csv")

    manager.add_expense("Coffee", 120.0, "Food", "2026-07-25")
    manager.add_expense("Pizza", 350.0, "Food", "2026-07-25")

    # Delete first expense (0-based index)
    assert manager.delete_expense(0) is True

    remaining = manager.get_all_expenses()
    assert len(remaining) == 1
    assert remaining[0].title == "Pizza"


def test_delete_expense_invalid_index(tmp_path):
    manager = ExpenseManager()
    manager.storage = CSVStorage(tmp_path / "expenses.csv")

    manager.add_expense("Coffee", 120.0, "Food", "2026-07-25")

    assert manager.delete_expense(-1) is False
    assert manager.delete_expense(5) is False


def test_delete_from_empty(tmp_path):
    manager = ExpenseManager()
    manager.storage = CSVStorage(tmp_path / "expenses.csv")

    assert manager.delete_expense(0) is False
