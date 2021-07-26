import numpy as np
import pandas as pd

class SelectionSort:
    def __init__(self,array):
        self.array=array
        self.swaps=[]
        self.swap_df=pd.DataFrame(array).T

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
            self.swap_df.loc[i+1,:]=self.array
            self.swaps.append([i,min_idx])
        return np.array(self.array)



# if __name__ == '__main__':
#     state = np.random.RandomState(88)
#     test_array = np.arange(10)
#     shuffled_test_array = state.permutation(test_array)
#     sorter = SelectionSort(shuffled_test_array)
#     sorted_array = sorter.run_sort()