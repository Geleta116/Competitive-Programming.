class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def hour(i,j):
            return sum(grid[i-1][j-1:j+2]) + grid[i][j] + sum(grid[i+1][j-1:j+2])
        num_rows = len(grid)
        num_cols = len(grid[0])
        out = float(-inf)
        i_index = 1
        
        while (i_index>0 and i_index<num_rows-1):
            j_index = 1
            while (j_index>0 and j_index<num_cols-1):
                out  = max(out, hour(i_index,j_index))
                j_index+=1
            i_index+=1
        
        return out
