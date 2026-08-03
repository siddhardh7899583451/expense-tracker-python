```markdown
# Sequence Diagram: Add Expense Flow

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant CLI as CLI App
    participant V as Validators
    participant EM as ExpenseManager
    participant S as CSVStorage
    participant File as expense.csv

    User->>CLI: Selects "Add Expense"
    CLI->>User: Prompts for Title, Amount, Category, Date
    User->>CLI: Inputs raw data
    
    CLI->>V: Validate inputs (Amount, Date)
    alt Validation Fails
        V-->>CLI: Return Error
        CLI-->>User: Display validation error
    else Validation Passes
        V-->>CLI: Return sanitized data
        CLI->>EM: add_expense(title, amount, category, date)
        EM->>EM: Instantiates Expense object
        EM->>S: save_expenses(expenses)
        S->>File: Write row to CSV
        File-->>S: File saved successfully
        S-->>EM: True
        EM-->>CLI: Success
        CLI-->>User: Display success message & updated table
    end