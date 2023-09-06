class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        goalRow1 = [1,2,3]
        goalRow2 = [4,5,0]
        
        # Data structures
        queue = deque()
        visited = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        # populating the data structures
        for row in range(2):
            for col in range(3):
                if board[row][col] == 0:
                    queue.append((board[0], board[1], row, col, 0))
                    visited.add(tuple([tuple(board[0]), tuple(board[1])]))
                    
        #helper functions
        def inbound(row, col):
            return 0 <= row < 2 and 0 <= col < 3
        
        # bfs part
        while queue:
            # print(queue)
            firstRow, secondRow, currRow,currCol,level = queue.popleft()
            
            if firstRow[:] == goalRow1[:] and secondRow[:] == goalRow2[:]:
                return level
            
            for addedRow, addedCol in directions:
                
                newRow = currRow + addedRow
                newCol = currCol + addedCol
                temp1 = [firstRow[:], secondRow[:]]
                
                
                if inbound(newRow, newCol):
                    temp1[currRow][currCol], temp1[newRow][newCol] = temp1[newRow][newCol], temp1[currRow][currCol]
                    if tuple([tuple(temp1[0]), tuple(temp1[1])]) not in visited:
                        visited.add(tuple([tuple(temp1[0]), tuple(temp1[1])]))
                        queue.append((temp1[0], temp1[1], newRow, newCol, level + 1))
        
                    
                    
        return -1
            
            
            
        