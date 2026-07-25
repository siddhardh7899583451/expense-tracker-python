from tabulate import tabulate


def display_expenses(expenses):
    """Display expenses in a formatted table."""

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


def display_monthly_summary(summary: dict):
    """Display formatted monthly expense summary."""
    month = summary["month"]
    total = summary["total"]
    categories = summary["categories"]

    print("\n" + "=" * 30)
    print("Monthly Summary")
    print("=" * 30)
    print(f"\nMonth: {month}")
    print(f"Total Expenses : ${total:,.2f}\n")

    if not categories:
        print("No expenses found for this month.\n")
        return

    print("Category Breakdown")
    print("-" * 30)

    for category, amt in categories.items():
        print(f"{category:<18} ${amt:,.2f}")

    print()