```markdown
# Architecture Diagram

```mermaid
graph TD
    subgraph Presentation & UI Layer
        MAIN[main.py Entrypoint]
        CLI[cli.py Controller]
        DISP[display.py View Helpers]
        UI[ui.py Component Wrapper]
        THEME[theme.py Styling Config]
    end

    subgraph Business Logic Layer
        EM[manager.py ExpenseManager]
        VAL[validators.py Input Sanitizer]
        MODEL[models.py Expense Domain Model]
    end

    subgraph Persistence Layer
        CS[storage.py CSVStorage]
        DATA[(data/expense.csv)]
    end

    MAIN --> CLI
    CLI --> DISP
    CLI --> VAL
    CLI --> EM
    
    DISP --> UI
    UI --> THEME

    EM --> MODEL
    EM --> CS
    CS --> DATA