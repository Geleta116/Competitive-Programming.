class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(len(board)):
            row_checker = set()
            for col in range(len(board)):
                if board[row][col]!="." and board[row][col] not in row_checker:
                    row_checker.add(board[row][col])
                elif  board[row][col]!="." and board[row][col] in row_checker:
                    return False
        
        for col in range(len(board)):
            col_checker = set()
            for row in range(len(board)):
                if board[row][col]!="." and board[row][col] not in col_checker:
                    col_checker.add(board[row][col])
                elif  board[row][col]!="." and board[row][col] in col_checker:
                    return False
        row = 0
        
        while row<9:
            col = 0
            while col <9:
                checker = set()
                for r in range(3):
                    for c in range(3):
                        if board[row+r][col+c]!="." and board[row+r][col+c] not in checker:
                             checker.add(board[row+r][col+c])
                        elif  board[row+r][col+c]!="." and board[row+r][col+c] in checker:
                            return False
               
                col += 3
            row += 3
       

        return True
                            
                        
        
        
        