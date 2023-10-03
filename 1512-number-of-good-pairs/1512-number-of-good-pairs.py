class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = 0
        dp = defaultdict(int)
        
        for num in nums:
            output += dp[num]
            dp[num] += 1
        return output
        