


class HeapSort:
    '''
    in place algorithm
    no additional memory
    O(nlog(n))

    '''
    def __init__(self,array):
        self.array=array

    def build_heap(self):
        '''
        build complete binary tree that satifies heap property on every edge
        :return:
        '''


        swaps = []
        for root in range(len( self.array) // 2 - 1, -1, -1):
            rootVal = self.array[root]
            child = 2 * root + 1
            while child < len( self.array):
                if child + 1 < len( self.array) and  self.array[child] >  self.array[child + 1]:
                    child += 1
                if rootVal <=  self.array[child]:
                    break

                self.array
                [child],  self.array[(child - 1) // 2] =  self.array[(child - 1) // 2],  self.array[child]
                swaps.append(((child - 1) // 2, child))
                child = child * 2 + 1


        self.swaps=swaps

    def run_sort(self):
        pass

