# Class Diagram

```mermaid
classDiagram
    class Theme {
        +PRIMARY_COLOR: str
        +SECONDARY_COLOR: str
        +ACCENT_COLOR: str
        +get_header_style()
    }

    class UI {
        +Theme theme
        +clear_screen()
        +render_header(title)
        +render_panel(content, title)
    }

    class Expense {
        +str id
        +str title
        +float amount
        +str category
        +str date
        +to_dict() dict
        +from_dict(data: dict) Expense
    }

    class CSVStorage {
        +str filepath
        +load_expenses() List~Expense~
        +save_expenses(expenses: List~Expense~) bool
    }

    class ExpenseManager {
        -CSVStorage storage
        -List~Expense~ expenses
        +add_expense(title, amount, category, date) Expense
        +get_all_expenses() List~Expense~
        +search_expenses(keyword) List~Expense~
        +edit_expense(expense_id, title, amount, category, date) bool
        +delete_expense(expense_id) bool
        +get_monthly_summary(year, month) dict
        +get_dashboard_stats() dict
    }

    class Validators {
        +validate_amount(amount_str) float
        +validate_date(date_str) str
        +validate_category(category_str) str
        +validate_id(expense_id) bool
    }

    class Display {
        -UI ui
        +show_welcome()
        +show_dashboard(stats)
        +render_table(expenses)
        +show_help()
        +show_about()
        +show_monthly_summary(summary_data)
    }

    class CLI {
        -ExpenseManager manager
        -Display display
        +run()
        +handle_add()
        +handle_view()
        +handle_search()
        +handle_edit()
        +handle_delete()
        +handle_summary()
    }

    UI "1" *-- "1" Theme : uses
    Display "1" o-- "1" UI : uses
    ExpenseManager "1" *-- "many" Expense : manages
    ExpenseManager "1" o-- "1" CSVStorage : uses
    CLI "1" --> "1" ExpenseManager : interacts with
    CLI "1" --> "1" Display : uses
    CLI ..> Validators : uses for input validation