from expense_tracker.constants import MENU
from expense_tracker.display import display_expenses
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

            display_expenses(expenses)

        elif choice == "3":
            print("\nSearch Expenses\n")

            print("1. Search by Title")
            print("2. Search by Category")

            option = input("Choose option: ").strip()

            if option == "1":
                keyword = input("Enter title keyword: ")
                results = manager.search_by_title(keyword)

            elif option == "2":
                keyword = input("Enter category: ")
                results = manager.search_by_category(keyword)

            else:
                print("\nInvalid option.\n")
                continue

            print()

            if not results:
                print("No matching expenses found.\n")
                continue

            display_expenses(results)

        elif choice == "4":
            print("\nDelete Expense selected.\n")

        elif choice == "5":
            print("\nMonthly Summary selected.\n")

        elif choice == "6":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.\n")