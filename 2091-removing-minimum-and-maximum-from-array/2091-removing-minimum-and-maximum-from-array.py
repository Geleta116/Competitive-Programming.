class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # maxi, mini = ,
        return min(max( nums.index(min(nums)),nums.index(max(nums))) + 1, len(nums) - min( nums.index(min(nums)),nums.index(max(nums))), len(nums) - max( nums.index(min(nums)),nums.index(max(nums))) + min( nums.index(min(nums)),nums.index(max(nums))) + 1)