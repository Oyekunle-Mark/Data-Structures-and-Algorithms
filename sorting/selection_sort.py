def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_index = i

        for j in range(current_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        arr[current_index], arr[smallest_index] = arr[smallest_index], arr[current_index]

    return arr
