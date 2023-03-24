class Solution:
    def findKthLargest(self, array: List[int], k: int) -> int:
        self.out = float("-inf")
        
        def quicksort(array, start, end):
            
            if start > end:
                return
            
            pivot_index = random.randint(start, end)
            array[start], array[pivot_index] = array[pivot_index], array[start]
            pivot = array[start]
            
            write = start + 1 
            for read in range(write, end + 1):
                if array[read] <= pivot:
                    array[read], array[write] = array[write], array[read]
                    write += 1
                    
                    
            array[start], array[write - 1] = array[write - 1], array[start]
            if len(array) - k == write - 1:
                self.out = array[write - 1]
                return
            
            if len(array) - k > write - 1:
                    quicksort(array, write, end)
            else:
                quicksort(array,start, write - 2)
                    
        quicksort(array, 0 , len(array)- 1)
        
        return self.out