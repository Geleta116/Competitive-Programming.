class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp = [matrix[0][:]]
        dp = [[1000000000000 for row in range(len(matrix))] for col in range(len(matrix[0]))]
        dp[0] = matrix[0][:]
        directions = [(-1,-1),(-1,0),(-1,1)]
        
        def inbound(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                
                for addedRow, addedCol in directions:
                    rowToCheck = row + addedRow
                    colToCheck = col + addedCol
                    if inbound(rowToCheck, colToCheck) and dp[row][col] > matrix[row][col] + dp[rowToCheck][colToCheck]:
                        dp[row][col] = matrix[row][col] + dp[rowToCheck][colToCheck]
                  
        return min(dp[-1])
                
        
        
        
        