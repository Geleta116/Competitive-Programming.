class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        space = [[0 for _ in range(n)] for i in range(m)]
        
        space[m - 1][n - 1] = 1
        directions = [(1,0), (0,1)]
        
        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        for row in range(m-1, -1,-1 ):
            for col in range(n - 1, -1, -1):
                # print(row, col)
                for addedRow, addedCol in directions:
                    
                        
                        newRow = row + addedRow
                        newCol = col + addedCol
                        
                        if inbound(newRow, newCol):
                            # print(newRow, newCol)
                            space[row][col] += space[newRow][newCol]
                            
        return space[0][0]
                
                
                
        
        
        