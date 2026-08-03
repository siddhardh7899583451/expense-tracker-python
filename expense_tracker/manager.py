from datetime import datetime
from expense_tracker.models import Expense
from expense_tracker.sqlite_storage import SQLiteStorage
from expense_tracker.storage import CSVStorage


class ExpenseManager:

    def __init__(self, storage=None):
        self.storage = storage if storage else SQLiteStorage()

    def add_expense(self, title, amount, category, date):
        expense = Expense(
            title=title,
            amount=amount,
            category=category,
            date=date,
        )
        self.storage.save(expense)
        return expense

    def get_all_expenses(self):
        return self.storage.load()

    def search_by_title(self, keyword: str):
        """Search expenses by title (case-insensitive)."""
        keyword = keyword.lower()
        return [
            expense
            for expense in self.get_all_expenses()
            if keyword in expense.title.lower()
        ]

    def search_by_category(self, category: str):
        """Search expenses by category (case-insensitive)."""
        category = category.lower()
        return [
            expense
            for expense in self.get_all_expenses()
            if category in expense.category.lower()
        ]

    def delete_expense(self, index: int) -> bool:
        """Delete an expense by 0-based index."""
        expenses = self.get_all_expenses()
        if index < 0 or index >= len(expenses):
            return False

        del expenses[index]
        self.storage.save_all(expenses)
        return True

    def get_dashboard_stats(self) -> dict:
        """Recommendation #2: Encapsulate dashboard metrics in Manager."""
        expenses = self.get_all_expenses()
        return {
            "date": datetime.now().strftime("%d %b %Y"),
            "month": datetime.now().strftime("%B %Y"),
            "records": len(expenses),
            "spent": sum(e.amount for e in expenses),
        }

    def get_monthly_summary(self, month: str) -> dict:
        """Calculate summary for a given month (YYYY-MM)."""
        expenses = self.get_all_expenses()
        monthly_expenses = [exp for exp in expenses if exp.date.startswith(month)]

        if not monthly_expenses:
            return {
                "month": month,
                "total": 0.0,
                "count": 0,
                "categories": {},
                "highest": None,
                "lowest": None,
            }

        total = sum(exp.amount for exp in monthly_expenses)
        categories = {}

        for expense in monthly_expenses:
            categories[expense.category] = (
                categories.get(expense.category, 0.0) + expense.amount
            )

        highest = max(monthly_expenses, key=lambda e: e.amount)
        lowest = min(monthly_expenses, key=lambda e: e.amount)

        return {
            "month": month,
            "total": total,
            "count": len(monthly_expenses),
            "categories": categories,
            "highest": highest,
            "lowest": lowest,
        }

    def update_expense(
        self,
        index: int,
        title: str,
        amount: float,
        category: str,
        date: str,
    ) -> bool:
        """Update an existing expense by index."""
        expenses = self.get_all_expenses()
        if index < 0 or index >= len(expenses):
            return False

        expense = expenses[index]
        expense.title = title
        expense.amount = amount
        expense.category = category
        expense.date = date

        self.storage.save_all(expenses)
        return True
