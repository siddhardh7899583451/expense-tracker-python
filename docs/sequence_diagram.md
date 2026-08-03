```markdown
# Sequence Diagram: Add Expense & Dashboard Flow

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant CLI as cli.py (CLI)
    participant V as validators.py
    participant EM as manager.py (ExpenseManager)
    participant S as storage.py (CSVStorage)
    participant D as display.py (Display)
    participant File as expense.csv

    User->>CLI: Launches App / Navigates Main Menu
    CLI->>EM: get_dashboard_stats()
    EM-->>CLI: Return total spent, count, recent items
    CLI->>D: show_welcome() & show_dashboard(stats)
    D-->>User: Render Dashboard UI with Rich Cards

    User->>CLI: Selects "1. Add Expense"
    CLI->>User: Prompts for Title, Amount, Category, Date
    User->>CLI: Submits raw input

    CLI->>V: validate_amount(), validate_date(), validate_category()
    alt Validation Fails
        V-->>CLI: Raise ValueError
        CLI->>D: Render error banner
        D-->>User: Display validation error message
    else Validation Passes
        V-->>CLI: Return sanitized data
        CLI->>EM: add_expense(title, amount, category, date)
        EM->>EM: Instantiate Expense model
        EM->>S: save_expenses(expenses)
        S->>File: Write rows to CSV
        File-->>S: Success confirmation
        S-->>EM: Return True
        EM-->>CLI: Return new Expense object
        CLI->>D: render_table([new_expense])
        D-->>User: Render success panel & Rich Table confirmation
    end