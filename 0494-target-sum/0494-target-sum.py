class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        self.out = 0
        # @cache
        found = defaultdict(int)
        
        def backtrack(summ, index):
            
            if index == len(nums):
                if summ == target:
                    self.out += 1
                    return 1
                return 0
            
            if (summ, index) in found:
                
                return found[(summ, index)]
            
            found[(summ, index)] = backtrack(summ + nums[index], index + 1) + backtrack(summ - nums[index], index + 1)
            return found[(summ, index)]
            
        return backtrack(0,0)
        
        # return self.out