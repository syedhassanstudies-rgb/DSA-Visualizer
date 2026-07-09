from typing import Generator

def linear_search(arr: list, target: int) -> Generator:
    if False: yield
    step = 0

    for i in range(len(arr)):
        step += 1
        found = (arr[i] == target)

        yield {
            "algorithm":   "linear_search",
            "array":       arr,
            "target":      target,
            "checking_at": i,
            "found":       found,
            "step":        step
        }

        if found:
            return


def binary_search(arr: list, target: int) -> Generator:
    if False: yield
    low  = 0
    high = len(arr) - 1
    step = 0

    while low <= high:
        step += 1
        mid   = (low + high) // 2
        found = (arr[mid] == target)

        yield {
            "algorithm": "binary_search",
            "array":     arr,
            "target":    target,
            "low":       low,
            "high":      high,
            "mid":       mid,
            "found":     found,
            "step":      step
        }

        if arr[mid] == target:
            return
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1