import os
import sqlite3

# Default path pointing to database/expense.db relative to project root
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "expense.db")


def get_connection(db_path=None):
    """Establishes and returns a connection to the SQLite database."""
    target_path = db_path or DB_PATH

    # Create directory if path is a file on disk
    if target_path != ":memory:":
        os.makedirs(os.path.dirname(target_path), exist_ok=True)

    conn = sqlite3.connect(target_path)
    conn.row_factory = sqlite3.Row  # Enables dict-like column access
    return conn


def init_db(db_path=None):
    """Initializes the database schema if tables do not exist."""
    conn = get_connection(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print(" Database initialized successfully.")
