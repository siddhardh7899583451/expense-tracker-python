import time
from rich.console import Console
from rich.table import Table

console = Console()
from expense_tracker.theme import BOLD, MUTED, PRIMARY, RESET, SECONDARY
from expense_tracker.ui import clear_screen, render_banner


def render_welcome_screen():
    clear_screen()
    print(f"{PRIMARY}══════════════════════════════════════════════{RESET}\n")
    print(f"          💰 {BOLD}EXPENSE TRACKER{RESET}\n")
    print("       Production CLI Version 2.1\n")
    print("      Developed by Siddhardh Kuncha\n")
    print(f"{PRIMARY}══════════════════════════════════════════════{RESET}")
    print("\nLoading...")
    time.sleep(1)


def render_main_menu(stats: dict):
    """Clean dashboard with live stats dict."""
    clear_screen()
    print(f"""{PRIMARY}═══════════════════════════════════════════════
             💰 EXPENSE TRACKER v2.1
═══════════════════════════════════════════════{RESET}
{BOLD}Today    :{RESET} {stats.get('date', '')}
{BOLD}Expenses :{RESET} {stats.get('records', 0)}
{BOLD}Spent    :{RESET} ₹{stats.get('spent', 0.0):,.2f}
{PRIMARY}───────────────────────────────────────────────{RESET}
  {BOLD}1.{RESET} ➕ Add Expense
  {BOLD}2.{RESET} 📋 View Expenses
  {BOLD}3.{RESET} 🔍 Search Expenses
  {BOLD}4.{RESET} ✏️ Edit Expense
  {BOLD}5.{RESET} 🗑️ Delete Expense
  {BOLD}6.{RESET} 📊 Monthly Summary
  {BOLD}7.{RESET} ❓ Help
  {BOLD}8.{RESET} ℹ️ About
  {BOLD}9.{RESET} 🚪 Exit
{PRIMARY}═══════════════════════════════════════════════{RESET}""")


def render_add_screen():
    """Recommendation #1: UI headers in display.py."""
    clear_screen()
    render_banner("Add New Expense", icon="➕")


def render_search_screen():
    """Recommendation #1: Dedicated search header."""
    clear_screen()
    render_banner("Search Expenses", icon="🔍")


def render_search_results(keyword: str, results: list):
    """Recommendation #3: Polished search summary."""
    print(f"\n{BOLD}Keyword :{RESET} {keyword}")
    print(f"{BOLD}Matches :{RESET} {len(results)}")
    print(f"{PRIMARY}───────────────────────────────────────────{RESET}\n")
    render_table(results)


def render_table(expenses):
    """Formats expense list in a structured tabular layout using Rich."""
    if not expenses:
        print(f"{MUTED}No records found.{RESET}")
        return

    table = Table(
        title="[bold blue]Expenses[/bold blue]",
        header_style="bold magenta",
        show_lines=True,
    )

    table.add_column("No", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", style="white")
    table.add_column("Amount", justify="right", style="green")
    table.add_column("Category", justify="center", style="yellow")
    table.add_column("Date", justify="center", style="blue")

    for idx, exp in enumerate(expenses, 1):
        title = exp.title if hasattr(exp, "title") else exp.get("title", "")
        amount = exp.amount if hasattr(exp, "amount") else exp.get("amount", 0.0)
        cat = exp.category if hasattr(exp, "category") else exp.get("category", "")
        date = str(exp.date if hasattr(exp, "date") else exp.get("date", ""))

        table.add_row(str(idx), title, f"₹{amount:,.2f}", cat, date)

    console.print(table)


def render_view_expenses_screen(expenses, total_records: int, total_spent: float):
    clear_screen()
    render_banner("All Expenses", icon="📋")

    avg_spent = (total_spent / total_records) if total_records > 0 else 0.0

    print(f"{BOLD}Total Records   :{RESET} {total_records}")
    print(f"{BOLD}Total Spent     :{RESET} ₹{total_spent:,.2f}")
    print(f"{BOLD}Average Expense :{RESET} ₹{avg_spent:,.2f}\n")

    render_table(expenses)


def render_delete_confirmation(expense) -> bool:
    """Recommendation #4: Enhanced delete screen with clear summary."""
    clear_screen()
    render_banner("Delete Expense", icon="🗑")

    print(f"{BOLD}Title    :{RESET} {expense.title}")
    print(f"{BOLD}Category :{RESET} {expense.category}")
    print(f"{BOLD}Amount   :{RESET} ₹{expense.amount:,.2f}")
    print(f"{BOLD}Date     :{RESET} {expense.date}\n")

    print(f"{SECONDARY}Are you sure?{RESET}")
    print(" [Y] Yes")
    print(" [N] No\n")

    choice = input("Choice: ").strip().upper()
    return choice == "Y"


def render_edit_screen(expense):
    """Recommendation #5: Clear edit guidance."""
    clear_screen()
    render_banner("Edit Expense", icon="✏️")

    print(f"{SECONDARY}── Current Values ──────────────────────────{RESET}")
    print(f"{BOLD}Title    :{RESET} {expense.title}")
    print(f"{BOLD}Amount   :{RESET} ₹{expense.amount:,.2f}")
    print(f"{BOLD}Category :{RESET} {expense.category}")
    print(f"{BOLD}Date     :{RESET} {expense.date}")
    print(f"{PRIMARY}───────────────────────────────────────────{RESET}\n")
    print(f"{MUTED}Press Enter to keep existing values.[...] {RESET}\n")


def render_monthly_summary(
    month_name: str,
    total_count: int,
    total_amount: float,
    categories: dict,
    highest=None,
    lowest=None,
):
    clear_screen()
    render_banner("Monthly Summary", icon="📊")

    avg_expense = (total_amount / total_count) if total_count > 0 else 0.0

    print(f"{BOLD}Month           :{RESET} {month_name}")
    print(f"{BOLD}Total Expenses  :{RESET} {total_count}")
    print(f"{BOLD}Total Amount    :{RESET} ₹{total_amount:,.2f}")
    print(f"{BOLD}Average Expense :{RESET} ₹{avg_expense:,.2f}\n")

    if categories:
        print(f"{SECONDARY}── Category Breakdown ──────────────────────{RESET}")
        for cat, amt in categories.items():
            print(f"{cat.ljust(18)} ₹{amt:>10,.2f}")

    if highest or lowest:
        print(f"\n{PRIMARY}───────────────────────────────────────────{RESET}")
        if highest:
            print(
                f"{BOLD}Highest Expense :{RESET} {highest.title} (₹{highest.amount:,.2f})"
            )
        if lowest:
            print(
                f"{BOLD}Lowest Expense  :{RESET} {lowest.title} (₹{lowest.amount:,.2f})"
            )


def render_help_screen():
    clear_screen()
    render_banner("Help & Guidance", icon="❓")

    print(f"{BOLD}1. Add Expense{RESET}")
    print("   Add a new expense with title, amount, category, and date.\n")

    print(f"{BOLD}2. View Expenses{RESET}")
    print("   Display all recorded expenses in a formatted table.\n")

    print(f"{BOLD}3. Search Expenses{RESET}")
    print("   Search by title keyword or category name.\n")

    print(f"{BOLD}4. Edit Expense{RESET}")
    print("   Modify an existing expense record by its index number.\n")

    print(f"{BOLD}5. Delete Expense{RESET}")
    print("   Remove an expense record from storage.\n")

    print(f"{BOLD}6. Monthly Summary{RESET}")
    print("   View monthly totals, category breakdowns, and key statistics.\n")

    print(f"{PRIMARY}───────────────────────────────────────────{RESET}")
    print(f"{BOLD}📅 Date Format:{RESET} YYYY-MM-DD (e.g., 2026-07-26)")
    print(f"{PRIMARY}───────────────────────────────────────────{RESET}\n")


def render_about_screen():
    """Displays project information."""
    clear_screen()
    render_banner("About", icon="ℹ️")

    print(f"{BOLD}Project:{RESET} Expense Tracker Python")
    print(f"{BOLD}Version:{RESET} 2.1")
    print(f"{BOLD}Developer:{RESET} Siddhardh Kuncha")
    print(f"{BOLD}Language:{RESET} Python 3.12")
    print(f"{BOLD}Framework:{RESET} Rich CLI")
    print(f"{BOLD}Storage:{RESET} CSV")
    print(f"{BOLD}Testing:{RESET} pytest")
    print(f"{BOLD}Formatter:{RESET} black")
    print(f"{BOLD}License:{RESET} MIT")

    print(
        "\nGitHub Repository:\n"
        "https://github.com/siddhardh7899583451/expense-tracker-python"
    )


def render_exit_screen():
    clear_screen()
    print(f"""{PRIMARY}═══════════════════════════════════════════════

         Thank you for using

           💰 EXPENSE TRACKER

        Have a productive day!

═══════════════════════════════════════════════{RESET}""")