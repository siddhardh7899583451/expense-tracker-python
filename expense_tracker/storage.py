import csv
import os
from typing import List, Optional
from expense_tracker.models import Expense


class CSVStorage:

    def __init__(self, filepath: str = "expenses.csv"):
        self.filepath = filepath
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.filepath):
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            with open(self.filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["expense_id", "title", "amount", "category", "date"])

    def load(self) -> List[Expense]:
        if not os.path.exists(self.filepath):
            return []

        expenses = []
        with open(self.filepath, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row:
                    continue
                expenses.append(
                    Expense(
                        expense_id=row.get("expense_id", row.get("id")),
                        title=row["title"],
                        amount=float(row["amount"]),
                        category=row["category"],
                        date=row["date"],
                    )
                )
        return expenses

    def save(self, expense: Expense) -> bool:
        file_exists = os.path.exists(self.filepath)
        with open(self.filepath, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists or os.path.getsize(self.filepath) == 0:
                writer.writerow(["expense_id", "title", "amount", "category", "date"])
            writer.writerow(
                [
                    expense.expense_id,
                    expense.title,
                    expense.amount,
                    expense.category,
                    expense.date,
                ]
            )
        return True

    def save_all(self, expenses: List[Expense]) -> bool:
        with open(self.filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["expense_id", "title", "amount", "category", "date"])
            for expense in expenses:
                writer.writerow(
                    [
                        expense.expense_id,
                        expense.title,
                        expense.amount,
                        expense.category,
                        expense.date,
                    ]
                )
        return True

    def update_expense(self, expense: Expense) -> bool:
        """Updates an expense in the CSV file."""
        expenses = self.load()
        for i, e in enumerate(expenses):
            if e.expense_id == expense.expense_id:
                expenses[i] = expense
                self.save_all(expenses)
                return True
        return False

    def delete_expense(self, expense_id: str) -> bool:
        """Deletes an expense from the CSV file by ID."""
        expenses = self.load()
        new_expenses = [e for e in expenses if e.expense_id != expense_id]

        if len(new_expenses) == len(expenses):
            return False

        self.save_all(new_expenses)
        return True

    def update_expense(self, expense: Expense) -> bool:
        """Update an expense by expense_id."""
        expenses = self.load()

        for i, existing in enumerate(expenses):
            if existing.expense_id == expense.expense_id:
                expenses[i] = expense
                self.save_all(expenses)
                return True

        return False

    def delete_expense(self, expense_id: str) -> bool:
        """Delete an expense by expense_id."""
        expenses = self.load()

        updated = [expense for expense in expenses if expense.expense_id != expense_id]

        if len(updated) == len(expenses):
            return False

        self.save_all(updated)
        return True
