from tabulate import tabulate


def display_expenses(expenses):
    """
    Display expenses in a formatted table.
    """

    if not expenses:
        print("No expenses found.\n")
        return

    rows = []

    for index, expense in enumerate(expenses, start=1):
        rows.append(
            [
                index,
                expense.title,
                f"{expense.amount:.2f}",
                expense.category,
                expense.date,
            ]
        )

    print(
        tabulate(
            rows,
            headers=["#", "Title", "Amount", "Category", "Date"],
            tablefmt="grid",
        )
    )

    print()
