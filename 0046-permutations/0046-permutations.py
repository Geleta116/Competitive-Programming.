class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        case = set()
        def backtrack(arr):
            if len(case) ==  len(nums):
                self.permutations.append(arr[:])
                return
            
            
            for index in range(len(nums)):
                if nums[index] in case:
                    continue
                arr.append(nums[index])
                case.add(nums[index])
                backtrack(arr)
                arr.pop()
                case.remove(nums[index])
        
        
        backtrack([])
        
       
        return self.permutations
        
         