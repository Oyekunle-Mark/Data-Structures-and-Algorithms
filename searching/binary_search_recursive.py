def binary_search_recursive(arr, target, low, high):
  middle = (low+high)//2

  if len(arr) == 0:
    return -1
