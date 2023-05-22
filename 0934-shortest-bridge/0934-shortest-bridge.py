class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        out = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 1:
                    out = 1
                    break
            if out:
                break
        def inbound(row, col):
            return 0<= row < len(grid) and 0 <= col < len(grid[0])
        
        def checker(parentRow, parentCol, row, col):
            return grid[parentRow][parentCol] != grid[row][col]
        
        queue = deque()
        queue.append((row,col))
        visited = set()
        visited.add((0,0))
        
        while queue:
            row, col = queue.popleft()
            grid[row][col] = 2
            
            for addedRow, addedCol in directions:
                newRow = row + addedRow
                newCol = col + addedCol
                
                if inbound(newRow, newCol) and grid[newRow][ newCol] == 1 and (newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    queue.append((newRow, newCol))
        queue = deque()
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 2:
                    queue.append((row,col))
                    visited.add((row, col))
        output = 0
        
        while queue:
           
            
            for _ in range(len(queue)):
                row, col = queue.popleft()
                

                for addedRow, addedCol in directions:
                    newRow = row + addedRow
                    newCol = col + addedCol
                    
                    if inbound(newRow, newCol) and grid[newRow][ newCol] != 0 and checker(row,col, newRow, newCol):
                        return output 

                    
                    elif inbound(newRow, newCol) and grid[row][ col] == 2 and (newRow, newCol) not in visited  :
                        visited.add((newRow, newCol))
                        queue.append((newRow, newCol))
                        grid[newRow][newCol] = 2
            output += 1
                        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                    
        
        