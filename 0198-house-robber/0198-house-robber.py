class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memoization = [0 for _ in range(len(nums) + 1)]
        memoization[0] = 0
        memoization[1] = nums[0]
        
        for i in range(1, len(nums) ):
            memoization[i + 1] = max(memoization[i], nums[i] + memoization[i - 1])
            
        return memoization[-1]
            
         
        