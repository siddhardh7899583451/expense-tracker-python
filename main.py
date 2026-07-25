from expense_tracker.models import Expense
from expense_tracker.storage import CSVStorage


def main():
    storage = CSVStorage()

    expense = Expense(
        title="Lunch",
        amount=250,
        category="Food",
    )

    storage.save(expense)

    print("Expense saved successfully!\n")

    print("All Expenses:\n")

    expenses = storage.load()

    for expense in expenses:
        print(expense)


if __name__ == "__main__":
    main()