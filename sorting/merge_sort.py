from typing import List

def merge(arrA, arrB):
    merged_arr = [None] * (len(arrA) + len(arrB))

    index = index_a = index_b = 0

    while index_a < len(arrA) and index_b < len(arrB):
        if arrA[index_a] < arrB[index_b]:
            merged_arr[index] = arrA[index_a]
            index_a += 1
            index += 1
        else:
            merged_arr[index] = arrB[index_b]
            index_b += 1
            index += 1

    while index_a < len(arrA):
        merged_arr[index] = arrA[index_a]
        index_a += 1
        index += 1

    while index_b < len(arrB):
        merged_arr[index] = arrB[index_b]
        index_b += 1
        index += 1

    return merged_arr

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2

    return merge(merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:]))
