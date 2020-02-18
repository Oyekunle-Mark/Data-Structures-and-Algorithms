def linear_search(arr, target):
    """Linear search
    """
    for index, value in enumerate(arr):
        if value == target:
            return index

    return -1
