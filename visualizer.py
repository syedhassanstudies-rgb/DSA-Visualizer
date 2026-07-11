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