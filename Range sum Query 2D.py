class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        columns = len(matrix[0])
        self.summ = [[0]*(columns+1) for r in range(rows+1)]
        
        for r in range(rows):
            pre = 0
            for c in range(columns):
                pre+=matrix[r][c]
                top = self.summ[r][c+1]
                self.summ[r+1][c+1] = pre + top
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        Bright = self.summ[row2+1][col2+1]
        Bleft = self.summ[row2+1][col1]
        Tright = self.summ[row1][col2+1]
        Tleft = self.summ[row1][col1]
        
        return Bright-Bleft-Tright+Tleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
