import sqlite3
from typing import List, Optional
import expense_tracker.database as db
from expense_tracker.models import Expense


class SQLiteStorage:

    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path
        # Reset memory connection for fresh isolated test instances
        if self.db_path == ":memory:":
            db._MEMORY_CONN = None
        db.init_db(self.db_path)

    def find_all(self) -> List[Expense]:
        conn = db.get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, amount, category, date FROM expenses ORDER BY date DESC"
        )
        rows = cursor.fetchall()
        if self.db_path != ":memory:":
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

    def load(self) -> List[Expense]:
        return self.find_all()

    def save(self, expense: Expense) -> bool:
        conn = db.get_connection(self.db_path)
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
            if self.db_path != ":memory:":
                conn.close()

    def update_expense(self, expense: Expense) -> bool:
        conn = db.get_connection(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                UPDATE expenses
                SET title = ?, amount = ?, category = ?, date = ?
                WHERE id = ?
                """,
                (
                    expense.title,
                    expense.amount,
                    expense.category,
                    expense.date,
                    expense.expense_id,
                ),
            )
            conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error:
            return False
        finally:
            if self.db_path != ":memory:":
                conn.close()

    def delete_expense(self, expense_id: str) -> bool:
        conn = db.get_connection(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error:
            return False
        finally:
            if self.db_path != ":memory:":
                conn.close()
