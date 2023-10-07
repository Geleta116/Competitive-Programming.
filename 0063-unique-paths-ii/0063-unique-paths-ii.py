class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[-1][-1] == 1:
            return 0
        dp = [[ 0 for _ in range(len(obstacleGrid[0]))] for __ in range(len(obstacleGrid))]
        
        dp[0][0] = 1
        def inbound(r, c):
            return 0 <= r < len(obstacleGrid) and 0 <= c < len(obstacleGrid[0])
        
        directions = [(-1,0), (0,-1)]
        
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if row == 0 and col== 0:
                    continue
                
                if obstacleGrid[row][col] ==  1:
                    dp[row][col] = 0
                    continue
                
                for addedRow, addedCol in directions:
                    newRow = row + addedRow
                    newCol = col + addedCol
                    
                    if inbound(newRow, newCol):
                        dp[row][col] += dp[newRow][newCol]
                        
        return dp[-1][-1]
                    
                
        