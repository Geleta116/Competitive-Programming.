class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        len_row = len(grid)
        len_cols = len(grid[0])
        
        rows = [0] * len_row
        cols = [0] * len_cols
        
        for i in range(len(rows)):
            for j in range(len(cols)):
                rows[i]+= grid[i][j]
                cols[j]+= grid[i][j]
        
        out = []
        for i in range(len_row):
                eachr = []
                for j in range(len_cols):
                    eachr.append(rows[i] + cols[j]- (len_cols - rows[i]) - (len_row -  cols[j]))
                out.append(eachr)
        return(out)
                    
                                   