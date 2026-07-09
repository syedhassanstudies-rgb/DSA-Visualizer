from typing import Generator

def bubble_sort(arr: list) -> Generator:
    if False: yield
    arr = arr.copy()
    n = len(arr)
    step = 0

    for pass_num in range(n - 1):
        for i in range(n - 1 - pass_num):
            step += 1
            swapped = False

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

            yield {
                "algorithm": "bubble_sort",
                "array":     arr.copy(),
                "comparing": (i, i + 1),
                "swapped":   swapped,
                "pass":      pass_num,
                "step":      step
            }

def insertion_sort(arr: list) -> Generator:
    if False:
        yield

    arr = arr.copy()
    step = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            step += 1
            arr[j + 1] = arr[j]

            yield {
                "algorithm": "insertion_sort",
                "array": arr.copy(),
                "key": key,
                "comparing_at": j,
                "step": step
            }

            j -= 1

        arr[j + 1] = key


def selection_sort(arr: list) -> Generator:
    if False: yield
    arr = arr.copy()
    n = len(arr)
    step = 0

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            step += 1

            if arr[j] < arr[min_index]:
                min_index = j

            yield {
                "algorithm":   "selection_sort",
                "array":       arr.copy(),
                "min_index":   min_index,
                "scanning_at": j,
                "placed_at":   i,
                "step":        step
            }

        arr[i], arr[min_index] = arr[min_index], arr[i]


def merge_sort(arr: list) -> Generator:
    arr = arr.copy()
    step_counter = [0]

    def _merge(arr, left, mid, right) -> Generator:
        left_sub  = arr[left    : mid + 1]
        right_sub = arr[mid + 1 : right + 1]
        i = j = 0
        k = left

        while i < len(left_sub) and j < len(right_sub):
            step_counter[0] += 1

            if left_sub[i] <= right_sub[j]:
                arr[k] = left_sub[i]
                i += 1
            else:
                arr[k] = right_sub[j]
                j += 1
            k += 1

            yield {
                "algorithm": "merge_sort",
                "array":     arr.copy(),
                "merging":   [left_sub[:], right_sub[:]],
                "step":      step_counter[0]
            }

        while i < len(left_sub):
            arr[k] = left_sub[i]
            i += 1
            k += 1

        while j < len(right_sub):
            arr[k] = right_sub[j]
            j += 1
            k += 1

        yield from []

    def _sort(arr, left, right) -> Generator:
        if left >= right:
            return

        mid = (left + right) // 2

        yield from _sort(arr, left, mid)
        yield from _sort(arr, mid + 1, right)
        yield from _merge(arr, left, mid, right)

        yield from []

    yield from _sort(arr, 0, len(arr) - 1)


def quick_sort(arr: list) -> Generator:
    arr = arr.copy()
    step_counter = [0]

    def _partition(arr, low, high, result) -> Generator:
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            step_counter[0] += 1

            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

            yield {
                "algorithm":   "quick_sort",
                "array":       arr.copy(),
                "pivot":       pivot,
                "pivot_index": high,
                "scanning_at": j,
                "step":        step_counter[0]
            }

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        result[0] = i + 1

        yield from []

    def _quick_sort_helper(arr, low, high) -> Generator:
        if low < high:
            result = [0]
            yield from _partition(arr, low, high, result)
            pivot_index = result[0]
            yield from _quick_sort_helper(arr, low, pivot_index - 1)
            yield from _quick_sort_helper(arr, pivot_index + 1, high)

        yield from []

    yield from _quick_sort_helper(arr, 0, len(arr) - 1)