from typing import Iterable

def binary_search_recursive(arr: Iterable[int], target: int, low: int, high: int) -> int:
    """Recursive binary search
    """

    if len(arr) == 0:
        return -1

    midpoint = (low + high) // 2

    if arr[midpoint] == target:
        return midpoint

    if arr[midpoint] > target:
        return binary_search_recursive(arr[:midpoint], target, low, midpoint - 1)
    else:
        return binary_search_recursive(arr[midpoint:], target, midpoint + 1, high)
