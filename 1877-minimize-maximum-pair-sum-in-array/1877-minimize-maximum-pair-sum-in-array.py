class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        
        out = 0
        left = 0
        right = len(nums)-1
        
        while left < right:
            out = max(out, nums[left] + nums[right])
            left += 1
            right -= 1
            
        return out