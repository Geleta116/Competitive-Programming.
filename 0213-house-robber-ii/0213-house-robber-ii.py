class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        
        def rob1(nums: List[int]) -> int:
        
            memoization = [0 for _ in range(len(nums) + 1)]
            memoization[0] = 0
            memoization[1] = nums[0]

            for i in range(1, len(nums) ):
                memoization[i + 1] = max(memoization[i], nums[i] + memoization[i - 1])

            return memoization[-1]
    
        first = rob1(nums[:-1])
        second = rob1(nums[1:])

        return max(first, second)
        