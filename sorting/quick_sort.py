def quick_sort(arr):
    if len(arr) == 1:
        return arr

    pivot = arr[0]
    arr_without_pivot = arr[1:]

    left_arr = [item for item in arr_without_pivot if item < pivot]
    right_arr = [item for item in arr_without_pivot if item >= pivot]

    return quick_sort(left_arr) + pivot + quick_sort(right_arr)
