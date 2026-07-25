# Expense Tracker Python

A command-line expense management application built using Python.

## Features

✅ Add expenses  
✅ View expenses  
✅ Search expenses  
✅ Edit expenses  
✅ Delete expenses  
✅ Monthly expense summary  
✅ CSV based storage  
✅ Input validation  
✅ Unit testing with pytest  

## Tech Stack

- Python 3.12
- pytest
- CSV Storage
- Black Formatter
- Git/GitHub

## Project Structure

```text
expense_tracker/
│
├── cli.py          # User interface
├── manager.py      # Business logic
├── models.py       # Expense model
├── storage.py      # CSV handling
├── validators.py   # Input validation
├── display.py      # Table formatting
└── constants.py    # Menu constants

tests/
├── test_manager.py
├── test_summary.py
├── test_update.py
├── test_display.py
└── test_validators.py

screenshots/
│
├── menu.png
├── add_expense.png
├── view_expenses.png
├── monthly_summary.png
└── edit_delete.png

Running the Project

1. Create Virtual Environment
python -m venv .venv

2. Activate Virtual Environment
Windows:
.venv\Scripts\activate
macOS/Linux:
source .venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run Application
python main.py

5. Run Tests
pytest