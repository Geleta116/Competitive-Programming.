class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # minus = [-1 for i in range(len(matrix[0]+1))]
        # matrix.insert(0,minus)
        for item in matrix:
            item.insert(0,-1)
        minus = [-1 for i in range(len(matrix[0]))]
        matrix.insert(0,minus)
        
        for row in range(1,len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] != matrix[row-1][col-1] and  matrix[row-1][col-1] != -1:
                    return False
        return True