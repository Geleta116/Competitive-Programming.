class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        queue = deque()
        visited = set()
        
        for row in range(len( mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))
                    visited.add((row, col))
        directions = [(0,1), (0,-1), (1,0) , (-1,0)]
        
        def inbound(row, col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])
        #output = [[list([float("inf") for i in range(len(mat[0]))])*len(mat[0])] * len(mat)]
        output = [[float("inf") for i in range(len(mat[0]))] for j in range(len(mat))]
        while queue:
            size = len(queue)
            
            for _ in range(size):
              
                row, col, level = queue.popleft()
                output[row][col] = level
                for addedRow, addedCol in directions:
                    newRow = row + addedRow
                    newCol = col + addedCol
                    
                    if inbound(newRow, newCol) and (newRow, newCol) not in visited:
                        visited.add((newRow, newCol))
                        if mat[newRow][newCol] == 1:
                            queue.append((newRow, newCol, level + 1))
                        else:
                            queue.append((newRow, newCol, 0))
        return output
                            
                        
                
                
                
                
        
        
      