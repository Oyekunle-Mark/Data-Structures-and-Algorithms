from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        for j in range(i + 1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr
