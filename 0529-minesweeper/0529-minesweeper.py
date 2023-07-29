class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        self.visited = set()
        direction = [(1,0),(0,1),(1,1),(-1,-1),(0,-1),(1,-1),(-1,0),(-1,1)]
        
        def inbound(row,col):
            return 0<= row < len(board) and 0 <= col < len(board[0])
        
        def dfs(row, col):
            if (row, col) in self.visited:
                return
            else:
                self.visited.add((row, col))
                
                if board[row][col] == "M":
                    board[row][col] = "X"
                    return
                else:
                    mineCount = 0
                    for addedRow, addedCol in direction:
                        newRow = row + addedRow
                        newCol = col + addedCol
                        if inbound(newRow, newCol) and board[newRow][newCol] == "M":
                            mineCount += 1
                    if mineCount > 0:
                        board[row][col] = str(mineCount)
                        return
                    else:
                        board[row][col] = "B"
                        for addedRow, addedCol in direction:
                            newRow = row + addedRow
                            newCol = col + addedCol
                            if inbound(newRow, newCol):
                                dfs(newRow, newCol)
                        return
        dfs(click[0],click[1])
        return board
                        
                        
                        
        