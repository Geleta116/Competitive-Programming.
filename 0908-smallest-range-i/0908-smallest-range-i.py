class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        start = 0
        while start < len(nums):
            nums[start] = nums[-1] - nums[start]
            start += 1
        # print(nums)
        for idx in range(len(nums)):
            if nums[idx] - 2 * k > 0:
                return nums[idx] - 2 * k
            return 0
        