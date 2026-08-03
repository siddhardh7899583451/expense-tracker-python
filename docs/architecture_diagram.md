```markdown
# Architecture Diagram

```mermaid
graph TD
    subgraph Presentation Layer
        UI[User Interface / Rich Terminal]
        CLI[CLI Entrypoint main.py]
        Display[Display & Rich Helpers]
    end

    subgraph Business Logic Layer
        EM[ExpenseManager]
        VAL[Validators]
    end

    subgraph Data Layer
        CS[CSVStorage]
        DB[(expense.csv)]
    end

    UI --> CLI
    CLI --> Display
    CLI --> VAL
    CLI --> EM
    EM --> CS
    CS --> DB