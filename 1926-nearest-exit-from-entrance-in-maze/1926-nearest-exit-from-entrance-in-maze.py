class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        visited = set()
        directions = [(1,0) , (0,1), (-1,0), (0, -1)]  
        def isexit(row, col):
            care = (row != entrance[0]) or (col != entrance[1])
            
            store = care and (0 <= row < len(maze)) and  ( 0 <= col < len(maze[0]))
            
            if store:
                if  0 == row or row == len(maze) - 1 or col == 0 or col == len(maze[0]) - 1:
                    return True
            return False
        
        def inbound(row, col):
            return  (0 <= row < len(maze)) and  ( 0 <= col < len(maze[0]))
            
        x= entrance[0]
        y = entrance [1]
        visited.add((x,y))
        queue.append((x,y,0))
        
        while queue:
            row,col, level = queue.popleft()
           
            if isexit(row,col):
                return level
            
            for addedRow, addedCol in directions:
                newRow = row + addedRow
                newCol = col + addedCol
                if inbound(newRow, newCol) and (newRow, newCol) not in visited and maze[newRow][newCol] == ".":
                    visited.add((newRow, newCol))
                    queue.append((newRow, newCol, level + 1))
        
        return -1
            
            