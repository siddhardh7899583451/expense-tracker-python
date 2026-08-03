import sqlite3
from typing import Optional

_MEMORY_CONN: Optional[sqlite3.Connection] = None


def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    global _MEMORY_CONN

    # If testing with :memory:, reuse the same connection so tables persist
    if db_path == ":memory:":
        if _MEMORY_CONN is None:
            _MEMORY_CONN = sqlite3.connect(":memory:")
            _MEMORY_CONN.row_factory = sqlite3.Row
        return _MEMORY_CONN

    path = db_path if db_path else "database/expense.db"
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: Optional[str] = None):
    """Creates the expenses table if it does not already exist."""
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
        """)
    conn.commit()
    if db_path != ":memory:":
        conn.close()
