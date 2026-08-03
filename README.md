# 💰 Expense Tracker Python (CLI v3.0)

A modular, test-driven Python command-line application built with clean architectural principles.

Track daily expenses using either SQLite or CSV storage through an interchangeable Strategy Pattern architecture.

---

## ✨ Features

- 📊 Dashboard
- ➕ Add Expense
- ✏️ Edit Expense
- ❌ Delete Expense
- 📋 View Expenses
- 🔍 Search by Title
- 📂 Search by Category
- 📈 Monthly Summary
- 🛡️ Input Validation
- 💾 SQLite Storage
- 📄 CSV Storage
- 🔄 CSV → SQLite Migration
- 🧪 Unit Tested
- 🎨 Rich CLI Interface

---

## 🛠 Tech Stack

| Technology | Used |
|------------|------|
| Python 3.12 | ✅ |
| SQLite | ✅ |
| CSV | ✅ |
| Pytest | ✅ |
| Black | ✅ |
| Git | ✅ |
| GitHub | ✅ |

---

## 📁 Project Structure

```text
expense-tracker-python/
│
├── database/
│   └── expense.db (generated locally)
│
├── expense_tracker/
│   ├── cli.py
│   ├── constants.py
│   ├── database.py
│   ├── display.py
│   ├── manager.py
│   ├── migrate.py
│   ├── models.py
│   ├── sqlite_storage.py
│   ├── storage.py
│   ├── theme.py
│   ├── ui.py
│   └── validators.py
│
├── tests/
│
├── docs/
│
├── CHANGELOG.md
├── README.md
├── requirements.txt
└── main.py
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/siddhardh7899583451/expense-tracker-python.git

cd expense-tracker-python
```

---

### Create Virtual Environment

Windows

```cmd
python -m venv .venv
```

Activate

```cmd
.venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Application

```bash
python main.py
```

---

### Run Tests

```bash
python -m pytest
```

---

### Format Code

```bash
python -m black .
```

---

### CSV to SQLite Migration

```bash
python -m expense_tracker.migrate
```

---

## 📐 UML Documentation

| Document | Status |
|-----------|--------|
| Use Case Diagram | ✅ |
| Class Diagram | ✅ |
| Sequence Diagram | ✅ |
| Architecture Diagram | ✅ |

---

## 📊 Version History

### v1.0

- CSV Storage
- CRUD

### v2.0

- Rich CLI
- Dashboard
- Monthly Summary

### v2.1

- UML Documentation

### v3.0

- SQLite
- Strategy Pattern
- Migration Utility

---

## 🚀 Future Roadmap

### v4.0

Flask REST API

### v5.0

Authentication

### v6.0

SQLAlchemy

### v7.0

Docker

### v8.0

CI/CD

### v9.0

Cloud Deployment

### v10.0

React Dashboard

---

## 📄 License

MIT License