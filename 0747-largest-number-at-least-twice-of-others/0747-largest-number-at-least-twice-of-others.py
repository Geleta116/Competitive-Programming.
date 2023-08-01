class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        temp = nums[:]
        nums.sort()
        if nums[-1] >= nums[-2] * 2:
            return temp.index(nums[-1])
        return -1
        