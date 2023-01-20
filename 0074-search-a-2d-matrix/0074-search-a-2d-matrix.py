class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        low_pointer = 0
        high_pointer = row *col -1
        while low_pointer <= high_pointer:
            mid_pointer = (low_pointer + high_pointer)//2
            compare = matrix[mid_pointer//col][mid_pointer%col]
            if compare  == target:
                return True
            elif compare <target:
                low_pointer = mid_pointer+1
            elif compare >target:
                high_pointer = mid_pointer-1
        
       