class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix = 0
        out = 0
        for i in range(len(nums)):
            prefix += nums[i]
            out = max(out, math.ceil(prefix / (i + 1)))
        return out