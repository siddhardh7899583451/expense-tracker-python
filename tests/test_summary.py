from expense_tracker.manager import ExpenseManager
from expense_tracker.sqlite_storage import SQLiteStorage


def test_get_monthly_summary_single_expense():
    storage = SQLiteStorage(":memory:")
    manager = ExpenseManager(storage=storage)

    manager.add_expense("Coffee", 120.0, "Food", "2026-07-25")

    summary = manager.get_monthly_summary("2026-07")

    assert summary["month"] == "2026-07"
    assert summary["total"] == 120.0
    assert summary["categories"] == {"Food": 120.0}


def test_get_monthly_summary_multiple_categories():
    storage = SQLiteStorage(":memory:")
    manager = ExpenseManager(storage=storage)

    manager.add_expense("Coffee", 120.0, "Food", "2026-07-10")
    manager.add_expense("Pizza", 350.0, "Food", "2026-07-15")
    manager.add_expense("Bus", 50.0, "Travel", "2026-07-20")
    manager.add_expense("Book", 200.0, "Education", "2026-06-01")  # Different month

    summary = manager.get_monthly_summary("2026-07")

    assert summary["total"] == 520.0
    assert summary["categories"]["Food"] == 470.0
    assert summary["categories"]["Travel"] == 50.0
    assert "Education" not in summary["categories"]


def test_get_monthly_summary_empty():
    storage = SQLiteStorage(":memory:")
    manager = ExpenseManager(storage=storage)

    summary = manager.get_monthly_summary("2026-08")

    assert summary["total"] == 0.0
    assert summary["categories"] == {}
