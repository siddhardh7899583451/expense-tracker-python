# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by Keep a Changelog and follows Semantic Versioning.

---

# [v3.0] - 2026-08-03

## 🚀 Added

- SQLite database backend for persistent expense storage.
- SQLite connection manager (`database.py`).
- SQLite storage implementation (`sqlite_storage.py`).
- CSV to SQLite migration utility (`migrate.py`).
- UUID-based primary key (`expense_id`) for every expense.
- Strategy Pattern implementation allowing interchangeable storage engines.

---

## 🔄 Changed

- ExpenseManager now works independently of the storage backend.
- Added targeted SQL UPDATE operations.
- Added targeted SQL DELETE operations.
- Standardized CRUD operations across CSVStorage and SQLiteStorage.

---

## 🧪 Testing

- All unit tests passing.

```
15 passed in 0.14s
```

---

## 📦 Release

Version: **v3.0**

Highlights:

- SQLite Integration
- Strategy Pattern
- Migration Utility
- Improved Architecture