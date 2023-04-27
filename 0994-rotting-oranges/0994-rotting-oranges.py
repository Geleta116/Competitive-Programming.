class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        directions = [(0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0)]
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        numberFreshFruits = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    numberFreshFruits += 1
                    visited.add((row, col))
        
        queue = deque()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    
        minutes = 0
       
        while queue:
            size = len(queue)
            rotted = False
            for _ in range(size):
                rottenFruit = queue.popleft()


                for addedRow, addedCol in directions:
                    newRow = rottenFruit[0] + addedRow
                    newCol = rottenFruit[1] + addedCol

                    if inbound(newRow, newCol) :

                        if grid[newRow][newCol] == 1:
                            grid[newRow][newCol] = 2
                            rotted = True
                            numberFreshFruits -= 1
                            queue.append((newRow, newCol))
                        
            if rotted :
                minutes += 1
        
        if numberFreshFruits == 0:
            return minutes
        return -1
                        
            
        
        
        
        
        
        
        