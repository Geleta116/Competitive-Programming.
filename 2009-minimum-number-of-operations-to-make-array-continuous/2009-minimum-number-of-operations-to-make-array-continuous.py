class Solution:
    def minOperations(self, nnums: List[int]) -> int:
        n = len(nnums)
        nums =  list(set(nnums))
        nums.sort()
        mini = n
        for idx in range(len(nums)):
            left = nums[idx]
            right  =  left + n - 1
            jdx  =  bisect.bisect_right(nums, right)
            mini = min(mini, n - jdx + idx)
            
        return mini