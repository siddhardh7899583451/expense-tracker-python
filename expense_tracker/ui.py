import os
from expense_tracker.theme import BOLD, ERROR, MUTED, PRIMARY, RESET, SUCCESS, WARNING


def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Pauses execution until user hits Enter."""
    input(f"\n{MUTED}Press Enter to continue...{RESET}")


def render_banner(title: str, icon: str = "💰", width: int = 42):
    """Renders a styled header block."""
    border = "═" * width
    centered_title = f"{icon}  {title.upper()}".center(width)

    print(f"{PRIMARY}{border}")
    print(f"{BOLD}{centered_title}")
    print(f"{PRIMARY}{border}{RESET}\n")


def print_success(message: str):
    print(f"{SUCCESS}✓ {message}{RESET}")


def print_error(message: str):
    print(f"{ERROR}✗ {message}{RESET}")


def print_warning(message: str):
    print(f"{WARNING}⚠ {message}{RESET}")
