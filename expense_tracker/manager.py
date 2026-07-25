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