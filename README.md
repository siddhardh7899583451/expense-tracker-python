# 💰 Expense Tracker Python (CLI v2.0)

A modular, test-driven Python command-line application built with clean architectural principles. Easily track daily expenses, view monthly analytics, and manage records through a rich interactive terminal interface.

---

## ✨ Features

- **📊 Dynamic Dashboard:** Real-time metrics including today's date, total records, and total amount spent.
- **➕ Expense Management:** Full CRUD operations (Add, View, Edit, Delete) with validation safety.
- **🔍 Search & Filter:** Quick search filtered by title keyword or category.
- **📈 Monthly Analytics:** Detailed summaries with category breakdowns, average spend, and highest/lowest records.
- **🛡️ Input Validation & Persistence:** Clean input sanitization backed by structured CSV file storage.
- **🎨 Rich Terminal UI:** Clean ASCII table layouts, styled banners, and consistent color themes.
- **🧪 Unit Tested:** Full test suite powered by `pytest` covering business logic, calculations, and updates.

---

## 🛠️ Tech Stack

- **Language:** Python 3.12+
- **Testing:** `pytest`
- **Formatting:** `black`
- **Storage:** CSV Engine (Abstracted for future DB migration)
- **VCS:** Git / GitHub

---

## 📁 Project Structure

```text
expense-tracker-python/
│
├── expense_tracker/
│   ├── cli.py          # Action routing and interactive loop
│   ├── manager.py      # Core business logic & analytics engine
│   ├── storage.py      # CSV storage handler
│   ├── models.py       # Expense data model
│   ├── validators.py   # Input validation rules
│   ├── display.py      # Terminal UI layout renderers
│   ├── ui.py           # Screen helpers, headers & banners
│   ├── theme.py        # Color and ANSI styling constants
│   └── constants.py    # Global configurations
│
├── tests/              # Unit test suite
│   ├── test_manager.py
│   ├── test_summary.py
│   ├── test_update.py
│   ├── test_display.py
│   └── test_validators.py
│
├── docs/
│   └── screenshots/    # Application screenshots
│
├── main.py             # Entrypoint
├── requirements.txt
└── README.md

## 🚀 Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/siddhardh7899583451/expense-tracker-python.git
cd expense-tracker-python
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python main.py
```

### 6. Run the Test Suite

```bash
python -m pytest
```

### 7. Format the Code

```bash
python -m black .
```

---

## 🚀 Future Improvements

- SQLite database integration
- Flask/FastAPI REST API
- React web dashboard
- User authentication
- Expense charts and analytics
- Docker support
- GitHub Actions CI/CD

---

## 📄 License

This project is licensed under the MIT License.