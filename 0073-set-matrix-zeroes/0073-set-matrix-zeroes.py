class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        cols = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows.append(row)
                    cols.append(col)
        out = [0 for i in range(len(matrix[0]))]
        
        for item in rows:
            matrix[item] = out
        for item in range(len(matrix)):
            
            for c in cols:
                matrix[item][c] = 0
                
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        