class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def dp(idx, count):
            
            if idx == 0 and count == steps:
                return 1
            
            if count == steps:
                return 0
            store = dp(idx, count + 1) 
            if idx < arrLen - 1:
                store  += dp(idx + 1, count + 1) 
            if idx > 0:
                store += dp(idx - 1, count + 1) 
            return (store) % (10**9 + 7)
        
        return dp(0,0) 
        