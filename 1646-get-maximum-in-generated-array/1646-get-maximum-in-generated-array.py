class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        self.dp = defaultdict(int)
        self.dp[0] = 0
        
        
        def getMax(n):
            if n == 0:
                return 0
            if n ==  1:
                self.dp[n] = 1
                return 1
            if n == 2:
                self.dp[n] =  1
                return 1
            if n in self.dp:
                return self.dp[n]
            if n % 2 == 0:
                self.dp[n] = getMax(n // 2)
            else:
                self.dp[n] = getMax(n // 2) + getMax(n // 2 + 1)
            return self.dp[n]
      
        for key in range(n + 1):
            getMax(key)
        return max(self.dp.values())
        