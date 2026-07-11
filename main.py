from sorting import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort
from searching import linear_search, binary_search
from stack import stack_operations_gen
from visualizer import run_visualizer
from ai_helper import get_ai_explanation

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

SORT_ALGORITHMS = {
    "1": ("Bubble Sort", bubble_sort),
    "2": ("Insertion Sort", insertion_sort),
    "3": ("Selection Sort", selection_sort),
    "4": ("Merge Sort", merge_sort),
    "5": ("Quick Sort", quick_sort),
}

SEARCH_ALGORITHMS = {
    "1": ("Linear Search", linear_search),
    "2": ("Binary Search", binary_search),
}

DEMO_OPERATIONS = [
    ("push", 10),
    ("push", 20),
    ("push", 30),
    ("peek", None),
    ("pop", None),
    ("push", 5),
    ("pop", None),
    ("pop", None),
    ("pop", None),
    ("pop", None),  # intentional empty pop — must handle gracefully
]


def get_valid_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print(f"{RED}Please enter a valid whole number.{RESET}")


def parse_array(prompt: str) -> list:
    while True:
        try:
            raw = input(prompt).strip()
            return [int(x) for x in raw.split()]
        except ValueError:
            print(f"{RED}Enter space-separated integers only  e.g.  5 3 1 4 2{RESET}")


def print_header() -> None:
    print(f"\n{BOLD}{CYAN}{'=' * 44}")
    print("           DSA VISUALIZER")
    print(f"{'=' * 44}{RESET}")


def print_menu() -> None:
    print(f"""
{BOLD}Main Menu:{RESET}
  {YELLOW}1{RESET}. Sort an array
  {YELLOW}2{RESET}. Search in an array
  {YELLOW}3{RESET}. Stack demo
  {YELLOW}4{RESET}. Exit
""")


def handle_sort() -> None:
    print(f"\n{BOLD}Choose sorting algorithm:{RESET}")
    for key, (name, _) in SORT_ALGORITHMS.items():
        print(f"  {YELLOW}{key}{RESET}. {name}")

    choice = input("Choice: ").strip()
    if choice not in SORT_ALGORITHMS:
        print(f"{RED}Invalid choice.{RESET}")
        return

    name, algo = SORT_ALGORITHMS[choice]
    arr = parse_array("Enter array (space-separated integers): ")

    if not arr:
        print(f"{RED}Array cannot be empty.{RESET}")
        return

    print(f"\n{BOLD}Running {name} on {arr}{RESET}")
    input("Press Enter to start...")

    gen = algo(arr)
    steps = run_visualizer(gen)

    ask = input(f"\n{CYAN}Get AI explanation? (y/n): {RESET}").strip().lower()
    if ask == "y":
        print(get_ai_explanation(name, arr, steps))


def handle_search() -> None:
    print(f"\n{BOLD}Choose search algorithm:{RESET}")
    for key, (name, _) in SEARCH_ALGORITHMS.items():
        print(f"  {YELLOW}{key}{RESET}. {name}")

    choice = input("Choice: ").strip()
    if choice not in SEARCH_ALGORITHMS:
        print(f"{RED}Invalid choice.{RESET}")
        return

    name, algo = SEARCH_ALGORITHMS[choice]
    arr = parse_array("Enter array (space-separated integers): ")

    if not arr:
        print(f"{RED}Array cannot be empty.{RESET}")
        return

    if choice == "2":
        arr.sort()
        print(f"{YELLOW}Binary search requires sorted input. Sorted: {arr}{RESET}")

    target = get_valid_int("Enter target value: ")

    print(f"\n{BOLD}Running {name} on {arr}  target={target}{RESET}")
    input("Press Enter to start...")

    gen = algo(arr, target)
    steps = run_visualizer(gen)

    ask = input(f"\n{CYAN}Get AI explanation? (y/n): {RESET}").strip().lower()
    if ask == "y":
        print(get_ai_explanation(name, arr, steps))


def handle_stack() -> None:
    print(f"\n{BOLD}Stack Demo — preset operations:{RESET}")

    for op, val in DEMO_OPERATIONS:
        label = f"{op}({val})" if val is not None else f"{op}()"
        print(f"  {YELLOW}{label}{RESET}")

    input("\nPress Enter to start...")

    gen = stack_operations_gen(DEMO_OPERATIONS)
    steps = run_visualizer(gen)

    ask = input(f"\n{CYAN}Get AI explanation? (y/n): {RESET}").strip().lower()
    if ask == "y":
        print(get_ai_explanation("Stack", DEMO_OPERATIONS, steps))


def main() -> None:
    print_header()

    while True:
        print_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            handle_sort()
        elif choice == "2":
            handle_search()
        elif choice == "3":
            handle_stack()
        elif choice == "4":
            print(f"\n{GREEN}Goodbye!{RESET}\n")
            break
        else:
            print(f"{RED}Invalid choice. Enter 1, 2, 3, or 4.{RESET}")


if __name__ == "__main__":
    main()

git 