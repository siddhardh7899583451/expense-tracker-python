# Use Case Diagram

## Project

Expense Tracker Python (CLI v2.0)

---

## Primary Actor

**User**

The user interacts with the Expense Tracker application to manage personal expenses.

---

## System Use Cases

- Add Expense
- View Expenses
- Search Expenses
- Edit Expense
- Delete Expense
- Monthly Summary
- Exit Application

---

## UML Diagram (PlantUML)

```plantuml
@startuml

left to right direction

actor User

rectangle "Expense Tracker System" {

  usecase "Add Expense" as UC1
  usecase "View Expenses" as UC2
  usecase "Search Expenses" as UC3
  usecase "Edit Expense" as UC4
  usecase "Delete Expense" as UC5
  usecase "Monthly Summary" as UC6
  usecase "Exit Application" as UC7

}

User --> UC1
User --> UC2
User --> UC3
User --> UC4
User --> UC5
User --> UC6
User --> UC7

@enduml
```

---

## Diagram Description

The user is the only actor in the system.

The user can:

- Add new expenses
- View all expenses
- Search existing expenses
- Edit expense details
- Delete expenses
- View monthly summaries
- Exit the application

All functionality is initiated by the user through the command-line interface.