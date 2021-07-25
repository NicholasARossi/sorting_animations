
import numpy as np

class SelectionSort:
    def __init__(self,array):
        self.array=array
    def run_sort(self) -> np.ndarray:

        for i in range(len(self.array)):

            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, len(self.array)):
                if self.array[min_idx] > self.array[j]:
                    min_idx = j

            # Swap the found minimum element with
            # the first element
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
