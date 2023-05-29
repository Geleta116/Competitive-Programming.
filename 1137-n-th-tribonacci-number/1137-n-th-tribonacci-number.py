class Solution:
    def tribonacci(self, n: int) -> int:
        
        self.dp = defaultdict(int)
        
        def tribonnaci(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            if n in self.dp:
                return self.dp[n]
            
            self.dp[n] = tribonnaci(n - 1) + tribonnaci(n - 2) + tribonnaci(n - 3)
            return self.dp[n]
        
        output =  tribonnaci(n)
        
        return output
    


        