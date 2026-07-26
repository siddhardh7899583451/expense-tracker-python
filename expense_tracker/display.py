from expense_tracker.theme import BOLD, MUTED, PRIMARY, RESET, SECONDARY
from expense_tracker.ui import clear_screen, render_banner


def render_main_menu(
    today_date: str = "",
    month_name: str = "",
    total_count: int = 0,
    total_spent: float = 0.0,
):
    """Renders the CLI v2 dashboard header and main navigation menu."""
    clear_screen()

    # If dashboard metrics are provided, display the dynamic stats header
    if today_date or month_name or total_count or total_spent:
        print(f"""{PRIMARY}═══════════════════════════════════════════════
             💰 EXPENSE TRACKER v2.0
═══════════════════════════════════════════════{RESET}
{BOLD}Date:{RESET} {today_date.ljust(10)} | {BOLD}Month:{RESET} {month_name}
{BOLD}Total Expenses:{RESET} {str(total_count).ljust(4)} | {BOLD}Total Spent:{RESET} ${total_spent:,.2f}
{PRIMARY}───────────────────────────────────────────────{RESET}
  {BOLD}1.{RESET} ➕ Add Expense
  {BOLD}2.{RESET} 📋 View Expenses
  {BOLD}3.{RESET} 🔍 Search Expenses
  {BOLD}4.{RESET} ✏️  Edit Expense
  {BOLD}5.{RESET} 🗑 Delete Expense
  {BOLD}6.{RESET} 📊 Monthly Summary
  {BOLD}7.{RESET} 🚪 Exit
{PRIMARY}═══════════════════════════════════════════════{RESET}""")
    else:
        # Fallback boxed menu layout
        print(f"""{PRIMARY}╔══════════════════════════════════════════════╗
║             {SECONDARY}💰 EXPENSE TRACKER{PRIMARY}              ║
║                  {MUTED}Version 2.0{PRIMARY}                ║
╠══════════════════════════════════════════════╣
║  {BOLD}1. ➕ Add Expense{RESET}{PRIMARY}                          ║
║  {BOLD}2. 📋 View Expenses{RESET}{PRIMARY}                        ║
║  {BOLD}3. 🔍 Search Expenses{RESET}{PRIMARY}                      ║
║  {BOLD}4. ✏️  Edit Expense{RESET}{PRIMARY}                        ║
║  {BOLD}5. 🗑 Delete Expense{RESET}{PRIMARY}                       ║
║  {BOLD}6. 📊 Monthly Summary{RESET}{PRIMARY}                      ║
║  {BOLD}7. 🚪 Exit{RESET}{PRIMARY}                                ║
╚══════════════════════════════════════════════╝{RESET}""")


def render_table(expenses):
    """Formats expense list in a structured tabular layout."""
    if not expenses:
        print(f"{MUTED}No records found.{RESET}")
        return

    print(
        f"{PRIMARY}┌────┬──────────────────┬───────────┬───────────────┬────────────┐{RESET}"
    )
    print(
        f"{BOLD}│ No │ Title            │ Amount    │ Category      │ Date       │{RESET}"
    )
    print(
        f"{PRIMARY}├────┼──────────────────┼───────────┼───────────────┼────────────┤{RESET}"
    )

    for idx, exp in enumerate(expenses, 1):
        title = exp.get("title", "") if isinstance(exp, dict) else exp.title
        amount = exp.get("amount", 0.0) if isinstance(exp, dict) else exp.amount
        cat = exp.get("category", "") if isinstance(exp, dict) else exp.category
        date = exp.get("date", "") if isinstance(exp, dict) else exp.date

        print(
            f"│ {str(idx).ljust(2)} │ {title[:16].ljust(16)} │ ${amount:>8.2f} │ {cat[:13].ljust(13)} │ {str(date).ljust(10)} │"
        )

    print(
        f"{PRIMARY}└────┴──────────────────┴───────────┴───────────────┴────────────┘{RESET}"
    )


def render_view_expenses_screen(expenses, total_records: int, total_spent: float):
    """Dedicated screen view showing summary stats before rendering the expense table."""
    clear_screen()
    render_banner("All Expenses", icon="📋")

    avg_spent = (total_spent / total_records) if total_records > 0 else 0.0

    print(f"{BOLD}Total Records   :{RESET} {total_records}")
    print(f"{BOLD}Total Spent     :{RESET} ${total_spent:,.2f}")
    print(f"{BOLD}Average Expense :{RESET} ${avg_spent:,.2f}\n")

    render_table(expenses)


def render_delete_confirmation(expense) -> bool:
    """Displays a dedicated prompt layout to confirm deletion."""
    clear_screen()
    render_banner("Delete Expense", icon="🗑")

    title = expense.get("title", "") if isinstance(expense, dict) else expense.title
    amount = expense.get("amount", 0.0) if isinstance(expense, dict) else expense.amount
    cat = expense.get("category", "") if isinstance(expense, dict) else expense.category
    date = expense.get("date", "") if isinstance(expense, dict) else expense.date

    print(f"{BOLD}Title    :{RESET} {title}")
    print(f"{BOLD}Category :{RESET} {cat}")
    print(f"{BOLD}Amount   :{RESET} ${amount:,.2f}")
    print(f"{BOLD}Date     :{RESET} {date}\n")

    print(f"{SECONDARY}Are you sure you want to delete this item?{RESET}")
    choice = input("Confirm [Y/N]: ").strip().upper()
    return choice == "Y"


def render_edit_screen(expense):
    """Displays current expense attributes before gathering update inputs."""
    clear_screen()
    render_banner("Edit Expense", icon="✏️")

    title = expense.get("title", "") if isinstance(expense, dict) else expense.title
    amount = expense.get("amount", 0.0) if isinstance(expense, dict) else expense.amount
    cat = expense.get("category", "") if isinstance(expense, dict) else expense.category
    date = expense.get("date", "") if isinstance(expense, dict) else expense.date

    print(f"{SECONDARY}── Current Values ──────────────────────────{RESET}")
    print(f"{BOLD}Title    :{RESET} {title}")
    print(f"{BOLD}Amount   :{RESET} ${amount:,.2f}")
    print(f"{BOLD}Category :{RESET} {cat}")
    print(f"{BOLD}Date     :{RESET} {date}")
    print(f"{PRIMARY}───────────────────────────────────────────{RESET}\n")
    print(f"{MUTED}Leave blank to keep existing value.{RESET}\n")


def render_monthly_summary(
    month_name: str,
    total_count: int,
    total_amount: float,
    categories: dict,
    highest=None,
    lowest=None,
):
    """Renders the monthly breakdown dashboard screen."""
    clear_screen()
    render_banner("Monthly Summary", icon="📊")

    avg_expense = (total_amount / total_count) if total_count > 0 else 0.0

    print(f"{BOLD}Month           :{RESET} {month_name}")
    print(f"{BOLD}Total Expenses  :{RESET} {total_count}")
    print(f"{BOLD}Total Amount    :{RESET} ${total_amount:,.2f}")
    print(f"{BOLD}Average Expense :{RESET} ${avg_expense:,.2f}\n")

    if categories:
        print(f"{SECONDARY}── Category Breakdown ──────────────────────{RESET}")
        for cat, amt in categories.items():
            print(f"{cat.ljust(18)} ${amt:>10,.2f}")

    if highest or lowest:
        print(f"\n{PRIMARY}───────────────────────────────────────────{RESET}")
        if highest:
            h_title = (
                highest.get("title") if isinstance(highest, dict) else highest.title
            )
            h_amt = (
                highest.get("amount") if isinstance(highest, dict) else highest.amount
            )
            print(f"{BOLD}Highest Expense :{RESET} {h_title} (${h_amt:,.2f})")
        if lowest:
            l_title = lowest.get("title") if isinstance(lowest, dict) else lowest.title
            l_amt = lowest.get("amount") if isinstance(lowest, dict) else lowest.amount
            print(f"{BOLD}Lowest Expense  :{RESET} {l_title} (${l_amt:,.2f})")


def render_exit_screen():
    """Renders the exit screen graphic."""
    clear_screen()
    print(f"""{PRIMARY}═══════════════════════════════════════════════

         Thank you for using

           💰 EXPENSE TRACKER

        Have a productive day!

═══════════════════════════════════════════════{RESET}""")
