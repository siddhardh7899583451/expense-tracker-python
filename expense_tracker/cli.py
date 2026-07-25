from expense_tracker.constants import MENU


def run():
    while True:
        print(MENU)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\nAdd Expense selected.\n")

        elif choice == "2":
            print("\nView Expenses selected.\n")

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