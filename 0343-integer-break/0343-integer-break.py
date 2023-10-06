class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        @cache
        def dp(n):
            if n ==  1:
                return 1
            if n <= 3:
                return n
            
            maxi = 0
            
            for i in range(1, n):
                    
                    store = dp(i) * dp(n - i)
                    maxi = max(maxi, store)
                
            return maxi
        
        return dp(n)
