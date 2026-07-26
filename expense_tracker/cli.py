from expense_tracker.display import (
    render_add_screen,
    render_delete_confirmation,
    render_edit_screen,
    render_exit_screen,
    render_main_menu,
    render_monthly_summary,
    render_search_results,
    render_search_screen,
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
        # Step 2: Simplified menu rendering via manager stats
        stats = manager.get_dashboard_stats()
        render_main_menu(stats)

        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            # Add Expense
            render_add_screen()
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
            render_search_screen()
            print("1. Search by Title")
            print("2. Search by Category\n")

            option = input("Choose option (1-2): ").strip()

            if option == "1":
                keyword = input("Enter title keyword: ").strip()
                results = manager.search_by_title(keyword)
                render_search_results(keyword, results)
            elif option == "2":
                keyword = input("Enter category: ").strip()
                results = manager.search_by_category(keyword)
                render_search_results(keyword, results)
            else:
                print_error("Invalid option.")
            pause()

        elif choice == "4":
            # Recommendation #5: Edit with fallback to existing values
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
                    target = expenses[idx]

                    render_edit_screen(target)

                    raw_title = input(f"Title [{target.title}]: ").strip()
                    title = raw_title if raw_title else target.title

                    raw_amount = input(f"Amount [{target.amount}]: ").strip()
                    amount = float(raw_amount) if raw_amount else target.amount

                    raw_cat = input(f"Category [{target.category}]: ").strip()
                    category = raw_cat if raw_cat else target.category

                    raw_date = input(f"Date [{target.date}]: ").strip()
                    date = raw_date if raw_date else target.date

                    if manager.update_expense(idx, title, amount, category, date):
                        print_success("Expense updated successfully!")
                    else:
                        print_error("Failed to update expense.")
                else:
                    print_error("Invalid expense number.")
            except ValueError:
                print_error("Please enter valid input.")
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
                    target = expenses[idx]

                    if render_delete_confirmation(target):
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
