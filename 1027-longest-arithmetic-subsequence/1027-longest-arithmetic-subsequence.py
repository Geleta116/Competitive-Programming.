class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(lambda : 1)
        maxi = 2
        for right in range(len(nums)):
            for left in range(0,right):
                diff = nums[right] - nums[left]
                dp[(right,diff)] = dp[(left,diff)] + 1
                maxi = max(maxi, dp[(right,diff)])
        return maxi
                
        