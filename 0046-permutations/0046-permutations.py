class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        
        def backtrack(arr):
            if len(set(arr)) ==  len(nums):
                self.permutations.append(arr[:])
                return
            elif len(set(arr)) != len(arr):
                return
            
            for index in range(len(nums)):
                arr.append(nums[index])
                backtrack(arr)
                arr.pop()
        
        
        backtrack([])
        
       
        return self.permutations
        
         