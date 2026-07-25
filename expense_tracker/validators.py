from datetime import datetime


def get_valid_title() -> str:
    """Prompt until a non-empty title is provided."""
    while True:
        title = input("Title: ").strip()
        if title:
            return title
        print("Title cannot be empty.")


def get_valid_amount() -> float:
    """Prompt until a positive number is provided."""
    while True:
        raw_val = input("Amount: ").strip()
        try:
            val = float(raw_val)
            if val > 0:
                return val
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid amount.")


def get_valid_category() -> str:
    """Prompt until a non-empty category is provided."""
    while True:
        category = input("Category: ").strip()
        if category:
            return category
        print("Category cannot be empty.")


def get_valid_date() -> str:
    """Prompt until a valid YYYY-MM-DD date is provided or return today's date if empty."""
    while True:
        raw_date = input("Date (YYYY-MM-DD, leave blank for today): ").strip()
        if not raw_date:
            return datetime.today().strftime("%Y-%m-%d")

        try:
            valid_dt = datetime.strptime(raw_date, "%Y-%m-%d")
            return valid_dt.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date.\nUse YYYY-MM-DD.")


def get_valid_month() -> str:
    """Prompt user for a valid month in YYYY-MM format."""
    while True:
        month_str = input("Enter month (YYYY-MM): ").strip()

        try:
            # Validate format YYYY-MM
            datetime.strptime(month_str, "%Y-%m")
            return month_str
        except ValueError:
            print("Invalid month format. Please use YYYY-MM (e.g., 2026-07).\n")
