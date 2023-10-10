class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums =  list(set(nums))
        nums.sort()
        mini = n
        for idx in range(len(nums)):
            left = nums[idx]
            right  =  left + n - 1
            jdx  =  bisect.bisect_right(nums, right)
            mini = min(mini, n - jdx + idx)
            
        return mini