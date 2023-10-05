class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxi, mini = nums.index(max(nums)), nums.index(min(nums))
        return min(max(mini,maxi) + 1, len(nums) - min(mini,maxi), len(nums) - max(mini,maxi) + min(mini,maxi) + 1)