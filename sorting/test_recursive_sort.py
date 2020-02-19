import unittest
import random
from merge_sort import merge_sort
from quick_sort import quick_sort


class RecursiveSortingTests(unittest.TestCase):
    def test_merge_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [2]
        arr4 = [0, 1, 2, 3, 4, 5]
        arr5 = random.sample(range(200), 50)

        self.assertEqual(merge_sort(arr1), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(merge_sort(arr2), [])
        self.assertEqual(merge_sort(arr3), [2])
        self.assertEqual(merge_sort(arr4), [0, 1, 2, 3, 4, 5])
        self.assertEqual(merge_sort(arr5), sorted(arr5))

    def test_quick_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [2]
        arr4 = [0, 1, 2, 3, 4, 5]
        arr5 = random.sample(range(200), 50)

        self.assertEqual(quick_sort(arr1), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(quick_sort(arr2), [])
        self.assertEqual(quick_sort(arr3), [2])
        self.assertEqual(quick_sort(arr4), [0, 1, 2, 3, 4, 5])
        self.assertEqual(quick_sort(arr5), sorted(arr5))


if __name__ == '__main__':
    unittest.main()
