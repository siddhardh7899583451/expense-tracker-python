from datetime import date

from expense_tracker.constants import MENU
from expense_tracker.manager import ExpenseManager

manager = ExpenseManager()


def run():
    while True:
        print(MENU)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\nAdd Expense\n")

            title = input("Title: ").strip()
            amount = float(input("Amount: "))
            category = input("Category: ").strip()
            expense_date = input(
                "Date (YYYY-MM-DD, leave blank for today): "
            ).strip()

            if not expense_date:
                expense_date = str(date.today())

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