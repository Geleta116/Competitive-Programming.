class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        toprow, botrow, leftcol, rightcol = 0 , len(matrix) - 1, 0, len(matrix[0]) - 1
        output = []
        
        while toprow <= botrow and leftcol <= rightcol:
            
            for col in range(leftcol, rightcol + 1):
                output.append(matrix[toprow][col])
            toprow += 1
            
            for row in range(toprow, botrow + 1):
                output.append(matrix[row][rightcol])
            rightcol -= 1
            
            if toprow <= botrow:
                for col in range(rightcol , leftcol - 1, -1):
                    output.append(matrix[botrow][col])
                botrow -= 1
                
            if leftcol <= rightcol:
                for row in range(botrow, toprow - 1, -1):
                    output.append(matrix[row][leftcol])

                leftcol += 1
            
      
        return output