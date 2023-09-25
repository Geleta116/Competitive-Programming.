class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        @cache
        def dp(index, runningSum):
            if index >= len(stones):
                return abs(runningSum)
            
            pos = dp(index + 1, runningSum + stones[index])
            neg = dp(index + 1, runningSum - stones[index])
            
            return min(pos, neg) 
        
        return dp(0,0)
        