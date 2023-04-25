class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        
        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        self.visited = set()
        
        def dfs(row, col):
            
            board[row][col] = -1
            
            for addedRow,addedCol in directions:
                newRow = row + addedRow
                newCol = col + addedCol
                if inbound(newRow, newCol) :
                    if board[newRow][newCol] == "O":
                        dfs(newRow, newCol)
        
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == 0) or (row == len(board)- 1) or (col == 0) or (col == len(board[0]) - 1):
                    
                    if board[row][col] == "O":
                        
                        dfs(row, col)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == -1:
                    board[row][col] = "O"
            
            
            
            
        
        