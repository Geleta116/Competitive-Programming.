class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.out  = []
      
        def backtrack(index,arr):
            if list(arr) not in self.out:
                self.out.append(list(arr))
           
            if index >= len(nums):
                return
            
            backtrack(index + 1, arr)
            arr.append(nums[index])
            backtrack(index+1,arr)
            arr.pop()
        
        backtrack(0,[])
       
        return self.out
            
        