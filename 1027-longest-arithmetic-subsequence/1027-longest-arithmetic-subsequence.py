class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(lambda : 1)
        maxi = 2
        for i in range(len(nums)):
            for j in range(0,i):
                diff = nums[i] - nums[j]
                dp[(i,diff)] = dp[(j,diff)] + 1
                maxi = max(maxi, dp[(i,diff)])
        return maxi
                
        