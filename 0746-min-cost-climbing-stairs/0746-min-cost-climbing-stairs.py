class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.dp = defaultdict(int)
        
        def minCost(n):
            if n < 0:
                return 0
            if n == 0  or n == 1:
                return cost[n]
            if n in self.dp:
                return self.dp[n]
            
            self.dp[n] = cost[n] + min(minCost(n - 1), minCost(n - 2))
            return self.dp[n] 
        
        return min(minCost(len(cost) - 1), minCost(len(cost) - 2))
        