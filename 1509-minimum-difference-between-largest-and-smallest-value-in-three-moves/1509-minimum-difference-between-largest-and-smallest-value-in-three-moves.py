class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        output = float("inf")
        
        if len(nums) <= 4:
            return 0
        end = len(nums) -  4
        start = 0
        while end < len(nums):
            output = min(output, nums[end] - nums[start])
            end += 1
            start += 1

            
        return output
        
        
        
        