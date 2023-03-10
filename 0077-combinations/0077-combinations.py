class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.out = []
        start = 0
        self.arr = [num for num in range(1,n + 1)]
      
        def combinations(lis,start):
            if len(lis) == k:
                self.out.append(lis[:])
                return
            elif start >= n:
                return
            
            combinations(lis,start + 1)
            lis.append(self.arr[start - 1])
            combinations(lis, start + 1)
            lis.pop()
            
        combinations([], 0)
        return self.out
        
                 
           
                
                
        