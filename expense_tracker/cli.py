from datetime import datetime

from expense_tracker.display import (
    render_delete_confirmation,
    render_edit_screen,
    render_exit_screen,
    render_main_menu,
    render_monthly_summary,
    render_table,
    render_view_expenses_screen,
)
from expense_tracker.manager import ExpenseManager
from expense_tracker.ui import (
    clear_screen,
    pause,
    print_error,
    print_success,
    print_warning,
)
from expense_tracker.validators import (
    get_valid_amount,
    get_valid_category,
    get_valid_date,
    get_valid_month,
    get_valid_title,
)

manager = ExpenseManager()


def run():
    while True:
        # Generate live metrics for dashboard header
        today_date = datetime.now().strftime("%Y-%m-%d")
        current_month = datetime.now().strftime("%B %Y")
        all_expenses = manager.get_all_expenses()
        total_count = len(all_expenses)
        total_spent = sum(e.amount for e in all_expenses)

        render_main_menu(
            today_date=today_date,
            month_name=current_month,
            total_count=total_count,
            total_spent=total_spent,
        )

        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            # Add Expense
            clear_screen()
            print("═══════════════════════════════════════")
            print("          ➕ ADD NEW EXPENSE           ")
            print("═══════════════════════════════════════\n")

            title = get_valid_title()
            amount = get_valid_amount()
            category = get_valid_category()
            expense_date = get_valid_date()

            manager.add_expense(title, amount, category, expense_date)
            print_success("Expense added successfully!")
            pause()

        elif choice == "2":
            # View Expenses
            expenses = manager.get_all_expenses()
            if not expenses:
                clear_screen()
                print_warning("No expenses found.")
            else:
                render_view_expenses_screen(
                    expenses,
                    total_records=len(expenses),
                    total_spent=sum(e.amount for e in expenses),
                )
            pause()

        elif choice == "3":
            # Search Expenses
            clear_screen()
            print("═══════════════════════════════════════")
            print("          🔍 SEARCH EXPENSES           ")
            print("═══════════════════════════════════════\n")

            print("1. Search by Title")
            print("2. Search by Category\n")

            option = input("Choose option (1-2): ").strip()

            if option == "1":
                keyword = input("Enter title keyword: ").strip()
                results = manager.search_by_title(keyword)
            elif option == "2":
                keyword = input("Enter category: ").strip()
                results = manager.search_by_category(keyword)
            else:
                print_error("Invalid option.")
                pause()
                continue

            print(f"\nFound {len(results)} matching expenses:\n")
            render_table(results)
            pause()

        elif choice == "4":
            # Edit Expense
            expenses = manager.get_all_expenses()
            if not expenses:
                clear_screen()
                print_warning("No expenses available to edit.")
                pause()
                continue

            clear_screen()
            render_table(expenses)

            try:
                choice_num = int(input("\nEnter expense number to edit: ").strip())
                if 1 <= choice_num <= len(expenses):
                    idx = choice_num - 1
                    target_expense = expenses[idx]

                    # Show current values before collecting updates
                    render_edit_screen(target_expense)

                    title = get_valid_title()
                    amount = get_valid_amount()
                    category = get_valid_category()
                    date = get_valid_date()

                    if manager.update_expense(idx, title, amount, category, date):
                        print_success("Expense updated successfully!")
                    else:
                        print_error("Failed to update expense.")
                else:
                    print_error("Invalid expense number.")
            except ValueError:
                print_error("Please enter a valid number.")
            pause()

        elif choice == "5":
            # Delete Expense
            expenses = manager.get_all_expenses()
            if not expenses:
                clear_screen()
                print_warning("No expenses available to delete.")
                pause()
                continue

            clear_screen()
            render_table(expenses)

            try:
                choice_num = int(input("\nEnter expense number to delete: ").strip())
                if 1 <= choice_num <= len(expenses):
                    idx = choice_num - 1
                    target_expense = expenses[idx]

                    # Prompt confirmation before deletion
                    if render_delete_confirmation(target_expense):
                        manager.delete_expense(idx)
                        print_success("Expense deleted successfully!")
                    else:
                        print_warning("Deletion canceled.")
                else:
                    print_error("Invalid expense number.")
            except ValueError:
                print_error("Please enter a valid number.")
            pause()

        elif choice == "6":
            # Monthly Summary
            clear_screen()
            print("═══════════════════════════════════════")
            print("          📊 MONTHLY SUMMARY           ")
            print("═══════════════════════════════════════\n")

            month = get_valid_month()
            summary = manager.get_monthly_summary(month)

            if not summary["categories"]:
                print_warning(f"No expenses found for {month}.")
            else:
                render_monthly_summary(
                    month_name=summary["month"],
                    total_count=summary["count"],
                    total_amount=summary["total"],
                    categories=summary["categories"],
                    highest=summary["highest"],
                    lowest=summary["lowest"],
                )
            pause()

        elif choice == "7":
            # Exit
            render_exit_screen()
            break

        else:
            print_error("Invalid option. Please enter a number between 1 and 7.")
            pause()
