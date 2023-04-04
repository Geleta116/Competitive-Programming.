class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maximumxor = 0
        
        for num in nums:
            maximumxor |= num
        self.count = 0
        def backtrack(start,previous):
            
            if start >= len(nums):
                return
            
            for end in range(start ,len(nums)):
                if previous | nums[end] == maximumxor:
                    self.count += 1
                
                backtrack(end + 1,previous | nums[end])
                
            return 
               
            
        backtrack(0, 0)
        return self.count
                
                    
                
        