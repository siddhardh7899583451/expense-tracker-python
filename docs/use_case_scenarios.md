# Use Case Scenarios

## Project
Expense Tracker Python (CLI v2.0)

---

# Actor

**Primary Actor:** User

The user interacts with the Expense Tracker through the command-line interface to manage personal expenses.

---

# Use Case 1 – Add Expense

### Goal
Record a new expense.

### Preconditions

- Application is running.
- User selects "Add Expense".

### Main Flow

1. User selects **Add Expense**.
2. System asks for:
   - Title
   - Amount
   - Category
   - Date
3. User enters valid information.
4. System validates the inputs.
5. System saves the expense to the CSV file.
6. System displays a success message.

### Alternate Flow

- If any input is invalid:
  - System displays an error.
  - User is asked to enter the value again.

### Postcondition

The expense is stored successfully.

---

# Use Case 2 – View Expenses

### Goal

Display all saved expenses.

### Preconditions

At least one expense may exist.

### Main Flow

1. User selects **View Expenses**.
2. System loads all expenses.
3. System displays them in a formatted table.

### Alternate Flow

If no expenses exist:

- System displays

```
No expenses found.
```

### Postcondition

User can review all expenses.

---

# Use Case 3 – Search Expense

### Goal

Find expenses quickly.

### Main Flow

1. User selects Search.
2. User chooses:
   - Search by Title
   - Search by Category
3. User enters a keyword.
4. System searches matching records.
5. Matching expenses are displayed.

### Alternate Flow

No matching records found.

### Postcondition

Matching records are shown.

---

# Use Case 4 – Edit Expense

### Goal

Modify an existing expense.

### Main Flow

1. User selects Edit.
2. System displays all expenses.
3. User selects an expense.
4. Current values are shown.
5. User enters new values or presses Enter to keep existing values.
6. System validates the input.
7. Expense is updated.

### Postcondition

Expense is successfully modified.

---

# Use Case 5 – Delete Expense

### Goal

Remove an expense.

### Main Flow

1. User selects Delete.
2. System displays all expenses.
3. User selects an expense.
4. System asks for confirmation.
5. User confirms.
6. Expense is deleted.

### Alternate Flow

User selects No.

Deletion is cancelled.

### Postcondition

Expense is removed or remains unchanged.

---

# Use Case 6 – Monthly Summary

### Goal

View monthly spending statistics.

### Main Flow

1. User selects Monthly Summary.
2. User enters a month.
3. System calculates:
   - Total expenses
   - Total amount
   - Average expense
   - Category breakdown
   - Highest expense
   - Lowest expense
4. Results are displayed.

### Alternate Flow

No expenses exist for the selected month.

### Postcondition

Monthly statistics are displayed.

---

# Use Case 7 – Exit Application

### Goal

Close the application.

### Main Flow

1. User selects Exit.
2. System displays a goodbye message.
3. Program terminates.

### Postcondition

Application closes safely.

---

# Overall Use Case Summary

| Use Case | Description |
|----------|-------------|
| Add Expense | Create a new expense |
| View Expenses | Display all expenses |
| Search Expense | Find expenses |
| Edit Expense | Update existing expense |
| Delete Expense | Remove an expense |
| Monthly Summary | View monthly statistics |
| Exit | Close the application |