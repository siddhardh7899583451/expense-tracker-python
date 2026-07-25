from expense_tracker.models import Expense


def main():
    expense = Expense(
        title="Lunch",
        amount=250.0,
        category="Food"
    )

    print("Expense created successfully!")
    print(expense)


if __name__ == "__main__":
    main()