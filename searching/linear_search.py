from typing import Iterable


def linear_search(arr: Iterable[int], target: int) -> int:
    """Linear search
    """

    for index, value in enumerate(arr):
        if value == target:
            return index

    return -1
