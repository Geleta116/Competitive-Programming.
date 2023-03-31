class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        self.case = 0
        def backtrack(arr):
            
            if 2 ** len(nums)  - 1 == self.case: 
                self.permutations.append(arr[:])
                return
            
            
            for index in range(len(nums)):
                if 2 ** index & self.case:
                    continue
                arr.append(nums[index])
                temp = self.case
                self.case =  (1 << index) | self.case
                
                backtrack(arr)
                arr.pop()
                self.case = temp
                
                
        
        
        backtrack([])
        
       
        return self.permutations
        
         