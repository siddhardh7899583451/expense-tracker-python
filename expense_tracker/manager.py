from expense_tracker.models import Expense
from expense_tracker.storage import CSVStorage


class ExpenseManager:
    def __init__(self):
        self.storage = CSVStorage()

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