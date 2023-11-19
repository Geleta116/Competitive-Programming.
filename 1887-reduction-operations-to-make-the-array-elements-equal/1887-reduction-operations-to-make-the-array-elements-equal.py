class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        out = 0
        for idx in range(len(nums) - 2, -1, -1):
            if nums[idx] != nums[idx + 1]:
                out += len(nums) - (idx + 1)
        return out
        