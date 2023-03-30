class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = Counter(nums)
        listCount = []
        for keys in unique:
            listCount.append([unique[keys], keys])
        
        
        def quickSort(arr, start, end):
            if start >  end:
                return 
            pivotPoint = random.randint(start, end) 
            arr[pivotPoint], arr[start] =  arr[start], arr[pivotPoint]
            pivot = arr[start]
            
            write = start + 1 
            for read in range(write, end + 1):
                if arr[read] <= pivot:
                    arr[read], arr[write] = arr[write], arr[read]
                    write += 1
                    
            arr[start], arr[write - 1] = arr[write - 1], arr[start]
            if len(arr) - k  >= write - 1:
                quickSort(arr,write, end)
            else:
                
                quickSort(arr, start, write - 2)
            
                    
        
        quickSort(listCount, 0, len(listCount) - 1)
        
        output = []
        print(listCount)
        for index in range(len(listCount) - k  , len(listCount) ):
            
            output.append(listCount[index][1])
        return output
        
        
        
        