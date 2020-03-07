from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    arr_without_pivot = arr[:-1]

    left_arr = [item for item in arr_without_pivot if item < pivot]
    right_arr = [item for item in arr_without_pivot if item >= pivot]

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)
