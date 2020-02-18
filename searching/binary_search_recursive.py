def binary_search_recursive(arr, target, low, high):
    if len(arr) == 0:
        return -1

    if arr[low] == target:
        return low

    midpoint = (low + high) // 2

    if arr[midpoint] > target:
        return binary_search_recursive(arr, target, low, midpoint - 1)
    else:
        return binary_search_recursive(arr, target, midpoint + 1, high)
