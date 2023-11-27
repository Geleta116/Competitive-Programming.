class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkRow():
            for row in board:
                validDict = set()
                for num in row:
                    if num != ".":
                        if num not in validDict:
                            validDict.add(num)
                        else:
                            return False
            return True
            
        def checkCol():
            for row in range(9):
                validDict = set()
                for col in range(9):
                    # print(row, col)
                    if board[col][row] != ".":
                        if board[col][row] in validDict:
                            return False
                        else:
                            validDict.add(board[col][row])
                            
            return True
        
        def checkBox():
            for row in range(0,9,3):
                for col in range(0,9,3):
                    validDict = set()
                    for r in range(3):
                        for c in range(3):
                            if board[row + r][col + c] != ".":
                                if board[row + r][col + c] in validDict:
                                    return False
                                validDict.add(board[row + r][col + c])
            return True
        
        return checkRow() and checkCol() and checkBox()
                                
                            
                            
                            
        
        
                
                
        