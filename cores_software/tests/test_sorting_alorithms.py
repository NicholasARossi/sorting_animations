import unittest
import numpy as np
from cores_software.sorting_algorithms.selection_sort import SelectionSort

class TestSelectionSort(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = np.random.RandomState(88)
        cls.test_array = np.arange(10)
        cls.shuffled_test_array = cls.state.permutation(cls.test_array)


    def test_sorting(self):
        sorter=SelectionSort(self.shuffled_test_array)
        sorted_array = sorter.run_sort()

        np.testing.assert_array_equal(self.test_array,sorted_array)