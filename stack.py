from typing import Generator


class Stack:
    def __init__(self) -> None:
        self._items = []

    def push(self, value) -> None:
        self._items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        top = self._items[-1] if self._items else None
        return f"Stack(top={top}, size={len(self._items)})"


def stack_operations_gen(operations: list) -> Generator:
    if False: yield
    stack = Stack()
    step  = 0

    for op, value in operations:
        step += 1
        result = None

        if op == "push":
            stack.push(value)
            result = None
        elif op == "pop":
            try:    result = stack.pop()
            except IndexError: result = "Error"
        elif op == "peek":
            try:    result = stack.peek()
            except IndexError: result = "Error"

        yield {
            "algorithm": "stack",
            "operation": op,
            "input": value,
            "result": result,
            "stack_state": stack._items[:],
            "step": step
        }