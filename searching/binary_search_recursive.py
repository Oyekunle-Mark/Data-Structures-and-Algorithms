def binary_search_recursive(arr, target, low, high):
    if len(arr) == 0:
        return -1

    midpoint = (low + high) // 2

    if arr[midpoint] == target:
        return midpoint

    if arr[midpoint] > target:
        return binary_search_recursive(arr[:midpoint], target, low, midpoint - 1)
    else:
        return binary_search_recursive(arr[midpoint:], target, midpoint + 1, high)
