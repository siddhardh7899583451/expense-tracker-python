from expense_tracker.manager import ExpenseManager
from expense_tracker.sqlite_storage import SQLiteStorage


def test_delete_expense_success():
    storage = SQLiteStorage(":memory:")
    manager = ExpenseManager(storage=storage)

    manager.add_expense("Coffee", 120.0, "Food", "2026-07-25")
    manager.add_expense("Pizza", 350.0, "Food", "2026-07-25")

    # Delete first expense (0-based index)
    assert manager.delete_expense(0) is True

    remaining = manager.get_all_expenses()
    assert len(remaining) == 1
    assert remaining[0].title == "Pizza"


def test_delete_expense_invalid_index():
    storage = SQLiteStorage(":memory:")
    manager = ExpenseManager(storage=storage)

    manager.add_expense("Coffee", 120.0, "Food", "2026-07-25")

    assert manager.delete_expense(-1) is False
    assert manager.delete_expense(5) is False


def test_delete_from_empty():
    storage = SQLiteStorage(":memory:")
    manager = ExpenseManager(storage=storage)

    assert manager.delete_expense(0) is False
