import csv
from pathlib import Path
from expense_tracker.models import Expense


class CSVStorage:
    def __init__(self, filename="data/expenses.csv"):
        self.file = Path(filename)

        # Create the data folder if it doesn't exist
        self.file.parent.mkdir(parents=True, exist_ok=True)

        # Create CSV file with header if it doesn't exist or is empty
        if not self.file.exists() or self.file.stat().st_size == 0:
            with open(self.file, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["expense_id", "title", "amount", "category", "date"])

    def save(self, expense: Expense):
        with open(self.file, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    expense.expense_id,
                    expense.title,
                    expense.amount,
                    expense.category,
                    expense.date,
                ]
            )

    def save_all(self, expenses):
        """Overwrite the CSV file with the updated list of expenses."""
        with open(self.file, "w", newline="", encoding="utf-8") as f:
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

    def load(self):
        # Return empty list if file doesn't exist or is empty
        if not self.file.exists() or self.file.stat().st_size == 0:
            return []

        expenses = []

        with open(self.file, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                expenses.append(
                    Expense(
                        title=row["title"],
                        amount=float(row["amount"]),
                        category=row["category"],
                        date=row["date"],
                        expense_id=row["expense_id"],
                    )
                )

        return expenses