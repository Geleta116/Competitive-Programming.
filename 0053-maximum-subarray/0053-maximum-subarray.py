class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxi = max(nums)
        max_run = 0
        for i in range(len(nums)):
            max_run = max(max_run + nums[i], nums[i])
            maxi = max(maxi, max_run, nums[i])
        return maxi