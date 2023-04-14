class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def inbound(row, col):
            return 0<= row < len(grid2) and 0<= col < len(grid2[0]) and grid2[row][col] == 1
        
        self.visited = [[False for i in range(len(grid1[0]))] for j in range(len(grid1))]
        self.count = 0
      
            
        def dfs(row, col):
            self.visited[row][col] = True
            
            if grid2[row][col] and grid2[row][col] != grid1[row][col]:
                self.status  =  False
            
            if not grid2[row][col]:
                return 
                
            
            for direction in directions:
                    
                    addedRow = direction[0]
                    addedCol = direction[1]
                    newRow = row + addedRow
                    newCol = col + addedCol
                    
                    if inbound(newRow, newCol) and not self.visited[newRow][newCol]:
                        if grid2[row][col] and grid2[newRow][newCol] != grid1[newRow][newCol]:
                            self.status  =  False
                        dfs(newRow, newCol)
            if self.status:
                return True
                        
            
        
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if not self.visited[row][col]:
                    self.status = True
                    store = dfs(row, col)
                    if store:
                        
                        self.count += 1
        
        return self.count
                    
            
        
        
        
        
        
