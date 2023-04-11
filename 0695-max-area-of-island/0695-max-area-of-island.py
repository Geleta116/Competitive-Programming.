class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(0,-1), (0,1), (1,0),(-1,0)]
        
        self.visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        
        
        def inbound(row, col):
            if 0 <=  row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col]:
                return True
            return False
        
        
        self.area = 0
        
        def dfs(row, col):
            
            if row > len(grid) or col > len(grid[0]):
                return 0
            
            self.visited[row][col] = True
            
            currentSum = 1
            
            for addedRow, addedCol in directions:
                
                newRow = row + addedRow
                newCol = col + addedCol
                
                if inbound(newRow, newCol) and not self.visited[newRow][newCol]:
                    currentSum += dfs(newRow, newCol)
                    
            self.area = max( self.area, currentSum )
            return currentSum
                    
                    
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] and not self.visited[row][col] :
                    s = dfs(row,col)
                   
        
        return self.area