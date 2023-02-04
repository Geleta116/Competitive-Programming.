
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for row in range(len(matrix)):
            for col in range(row):
                matrix[row][col] , matrix[col][row] = matrix[col][row], matrix[row][col]
                
        
        
                
       
        """
        Do not return anything, modify matrix in-place instead.
        """
        