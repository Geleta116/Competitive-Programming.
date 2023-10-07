class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.total = sum(nums)
        nums.sort(reverse = True)
        @cache
        def backtracking(nums, sum1, sum2):
            if sum1 == sum2 and not nums:
                return True
            if sum1 > self.total // 2 or sum2 > self.total:
                return False
            if not nums:
                return False
            
            left = backtracking(tuple(nums[1:]), sum1 + nums[0], sum2)
            
            if left:
                return left
            
            if not left:
                right = backtracking(tuple(nums[1:]), sum1, sum2 + nums[0])
                return right
        
        return backtracking(tuple(nums), 0, 0)
        