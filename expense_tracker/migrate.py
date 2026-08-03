import os

from expense_tracker.storage import CSVStorage
from expense_tracker.sqlite_storage import SQLiteStorage

csv_storage = CSVStorage()
sqlite_storage = SQLiteStorage()

expenses = csv_storage.load()

count = 0

for expense in expenses:
    sqlite_storage.save(expense)
    count += 1

print(f"✅ Successfully migrated {count} expense(s) to SQLite.")
