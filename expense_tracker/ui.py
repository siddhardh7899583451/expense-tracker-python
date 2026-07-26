import os
from colorama import Fore, Style, init

# Initialize colorama for cross-platform support
init(autoreset=True)


def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Pauses execution until the user presses Enter."""
    input(f"\n{Style.DIM}Press Enter to continue...{Style.RESET_ALL}")


def print_header(title: str):
    """Prints a styled header."""
    print(f"\n{Fore.CYAN}{Style.BRIGHT}{'=' * 40}")
    print(f"{title.center(40)}")
    print(f"{'=' * 40}{Style.RESET_ALL}\n")


def print_success(message: str):
    """Prints a success message."""
    print(f"{Fore.GREEN}✓ {message}{Style.RESET_ALL}")


def print_error(message: str):
    """Prints an error message."""
    print(f"{Fore.RED}✗ {message}{Style.RESET_ALL}")


def print_info(message: str):
    """Prints an informational message."""
    print(f"{Fore.BLUE}ℹ {message}{Style.RESET_ALL}")
