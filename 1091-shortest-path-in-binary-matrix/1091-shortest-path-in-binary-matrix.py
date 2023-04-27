class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[len(grid) - 1][len(grid[0]) - 1] == 1 or grid[0][0] == 1 :
            return -1
        
        visited = set()
        visited.add((0,0))
        queue = deque()
        queue.append((0,0,1))
        
        def inbound(row , col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) 
        directions = [(0,1), (0, -1) , (1, 0) , (-1, 0) , (1,1 ) , (1, -1), (-1,1), (-1, -1)]
        
        while queue:
            
            row, col, level = queue.popleft()
            if row == len(grid)-1 and col  ==  len(grid) - 1:
                return level
            for addedRow, addedCol in directions:
                
                newRow = row + addedRow
                newCol = col + addedCol
                
                
                if inbound(newRow, newCol) and (newRow, newCol) not in visited:
                    
                    if grid[newRow][newCol] == 0:
                        visited.add((newRow, newCol))
                        queue.append((newRow, newCol, level + 1))
                        
                        
                        
        return -1
                    
                        
                        
            
            
            
        
        
        
        