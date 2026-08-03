import sqlite3
from typing import List, Optional
from expense_tracker.models import Expense
from expense_tracker.database import get_connection, init_db


class SQLiteStorage:
    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path
        init_db(self.db_path)

    def load_expenses(self) -> List[Expense]:
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
                id=row["id"],
                title=row["title"],
                amount=row["amount"],
                category=row["category"],
                date=row["date"],
            )
            for row in rows
        ]

    def save_expense(self, expense: Expense) -> bool:
        """Inserts a new expense record into SQLite."""
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO expenses (id, title, amount, category, date) VALUES (?, ?, ?, ?, ?)",
                (
                    expense.id,
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

    def update_expense(self, expense: Expense) -> bool:
        """Updates an existing expense record."""
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE expenses SET title = ?, amount = ?, category = ?, date = ? WHERE id = ?",
            (expense.title, expense.amount, expense.category, expense.date, expense.id),
        )
        conn.commit()
        updated = cursor.rowcount > 0
        conn.close()
        return updated

    def delete_expense(self, expense_id: str) -> bool:
        """Deletes an expense record by ID."""
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        return deleted
