from expense_tracker.constants import MENU
from expense_tracker.manager import ExpenseManager
from expense_tracker.validators import (
    get_valid_amount,
    get_valid_category,
    get_valid_date,
    get_valid_title,
)

manager = ExpenseManager()


def run():
    while True:
        print(MENU)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\nAdd Expense\n")

            title = get_valid_title()
            amount = get_valid_amount()
            category = get_valid_category()
            expense_date = get_valid_date()

            manager.add_expense(
                title,
                amount,
                category,
                expense_date,
            )

            print("\nExpense added successfully!\n")

        elif choice == "2":
            expenses = manager.get_all_expenses()

            print()

            if not expenses:
                print("No expenses found.\n")
                continue

            for expense in expenses:
                print(expense)

            print()

        elif choice == "3":
            print("\nSearch Expenses selected.\n")

        elif choice == "4":
            print("\nDelete Expense selected.\n")

        elif choice == "5":
            print("\nMonthly Summary selected.\n")

        elif choice == "6":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.\n")
