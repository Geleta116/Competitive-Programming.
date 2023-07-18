class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = defaultdict(int)
        
        for i in arr:
            if i - difference in dp:
                dp[i] = dp[i - difference] + 1
            else:
                dp[i] = 1
        
        return max(dp.values())
                
        