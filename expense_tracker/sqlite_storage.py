import sqlite3
from typing import List, Optional
from expense_tracker.database import get_connection, init_db
from expense_tracker.models import Expense


class SQLiteStorage:

    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path
        init_db(self.db_path)

    def load(self) -> List[Expense]:
        """Fetches all expenses from the database."""
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, amount, category, date FROM expenses ORDER BY date DESC"
        )
        rows = cursor.fetchall()
        conn.close()

        return [
            Expense(
                expense_id=row["id"],
                title=row["title"],
                amount=row["amount"],
                category=row["category"],
                date=row["date"],
            )
            for row in rows
        ]

    def save(self, expense: Expense) -> bool:
        """Inserts a single expense into SQLite."""
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO expenses (id, title, amount, category, date) VALUES (?, ?, ?, ?, ?)",
                (
                    expense.expense_id,
                    expense.title,
                    expense.amount,
                    expense.category,
                    expense.date,
                ),
            )
            conn.commit()
            return True
        except sqlite3.Error:
            return False
        finally:
            conn.close()

    def save_all(self, expenses: List[Expense]) -> bool:
        """Replaces all records in the database with the provided expenses list.

        Used for batch operations like update and delete.
        """
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM expenses")
            for expense in expenses:
                cursor.execute(
                    "INSERT INTO expenses (id, title, amount, category, date) VALUES (?, ?, ?, ?, ?)",
                    (
                        expense.expense_id,
                        expense.title,
                        expense.amount,
                        expense.category,
                        expense.date,
                    ),
                )
            conn.commit()
            return True
        except sqlite3.Error:
            return False
        finally:
            conn.close()
