class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = []
        for row in range(len(grid)):
            temp = []
            for col in range(len(grid[0])):
                temp.append(-1)
            dp.append(temp[:])
        dp[-1][-1] = grid[-1][-1]
        
        def curr_cost(row, col):
            if row >= len(grid) or col >= len(grid[0]):
                return 20000000000
            elif dp[row][col] != -1:
                return dp[row][col]
            
            else:
                dp[row][col] = grid[row][col] +  min(curr_cost(row + 1, col), curr_cost(row, col + 1))
                return dp[row][col]
            
        for row in range(len(grid) - 1, -1, -1):
            for col in range(len(grid[0]) - 1, -1 , -1):
                if dp[row][col] == -1:
                    curr_cost(row, col)
        
        return dp[0][0]
        
        
                