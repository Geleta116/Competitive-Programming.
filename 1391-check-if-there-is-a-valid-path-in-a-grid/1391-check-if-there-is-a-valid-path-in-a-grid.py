class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
      
        up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
        
        
        queue = deque([(0,0)])
        visited =set([(0,0)])
        
        direction = {1:{left: left, right: right},
                    2:{up:up, down:down},
                    3:{right: down, up: left },
                    4:{up: right, left:down},
                    5:{right: up, down: left},
                    6:{down:right, left: up}}
        
        def inbound(row, col):
            if (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                return True
        
        m, n = len(grid), len(grid[0])
        while queue:
            
            row, col = queue.popleft()
            
            if row == m - 1  and col == n - 1:
                return True
            
            for addedRow, addedCol in direction[grid[row][col]].values():
                # print(direction[grid[row][col]].values())
                newRow = row + addedRow
                newCol = col + addedCol
                if inbound(newRow, newCol) and (newRow, newCol) not in visited and (addedRow, addedCol) in direction[grid[newRow][newCol]]:
                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))
#         print(visited)       
        return False
                    
                
                