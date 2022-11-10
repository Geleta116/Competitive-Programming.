class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        out = -1
        left = 0
        right = 1
        while right < len(nums):
            if nums[right]>nums[left]:
                out = max(out,nums[right]-nums[left])
            else:
                left = right
            right +=1
        return out
        