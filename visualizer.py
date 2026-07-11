GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"


def _format_array(arr: list, highlight: dict = None) -> str:
    highlight = highlight or {}
    parts = []
    for idx, val in enumerate(arr):
        if idx in highlight:
            color = highlight[idx]
            parts.append(f"{color}[{val}]{RESET}")
        else:
            parts.append(f" {val} ")
    return "[ " + "  ".join(parts) + " ]"


def print_step(step: dict) -> None:
    algorithm = step.get("algorithm", "unknown")
    print(f"\n{BOLD}Step {step['step']}{RESET}  ({algorithm})")

    if algorithm == "bubble_sort":
        i, j = step["comparing"]
        print(_format_array(step["array"], highlight={i: YELLOW, j: YELLOW}))
        swap_text = f"{RED}SWAPPED{RESET}" if step["swapped"] else "no swap"
        print(f"  comparing [{i}] and [{j}]  →  {swap_text}  (pass {step['pass']})")

    elif algorithm == "insertion_sort":
        print(_format_array(step["array"]))
        print(f"  inserting key={step['key']}  comparing at index {step['comparing_at']}")

    elif algorithm == "selection_sort":
        print(_format_array(step["array"], highlight={
            step["min_index"]: GREEN,
            step["scanning_at"]: YELLOW
        }))
        print(f"  filling position {step['placed_at']}  current min at index {step['min_index']}")

    elif algorithm == "merge_sort":
        print(_format_array(step["array"]))
        print(f"  merging: {step['merging'][0]}  +  {step['merging'][1]}")

    elif algorithm == "quick_sort":
        print(_format_array(step["array"], highlight={
            step["pivot_index"]: RED,
            step["scanning_at"]: YELLOW
        }))
        print(f"  pivot={step['pivot']}  scanning index {step['scanning_at']}")

    elif algorithm == "linear_search":
        print(_format_array(step["array"], highlight={step["checking_at"]: YELLOW}))
        if step["found"]:
            print(f"  {GREEN}FOUND{RESET} target={step['target']} at index {step['checking_at']}")
        else:
            print(f"  checking index {step['checking_at']}  no match")

    elif algorithm == "binary_search":
        print(_format_array(step["array"], highlight={step["mid"]: YELLOW}))
        print(f"  window [{step['low']}..{step['high']}]  mid={step['mid']}")
        if step["found"]:
            print(f"  {GREEN}FOUND{RESET} target={step['target']}")

    elif algorithm == "stack":
        print(f"  {step['operation']}({step['input']})")
        print(f"  stack (bottom → top): {step['stack_state']}")


def run_visualizer(gen) -> list:
    steps = []

    for step_dict in gen:
        print_step(step_dict)
        steps.append(step_dict)

    print(f"\n{BOLD}Total steps: {len(steps)}{RESET}")
    return steps
    