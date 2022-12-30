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
        print(rows)
        print(cols)
        out = []
        rowe = []
        cole = []
        for i  in rows:
            case = [i, len_cols - i]
            rowe.append(case)
        for i  in cols:
            case = [i, len_row - i]
            cole.append(case)
        print(rowe)
        print(cole)
        for i in range(len(rowe)):
            case = []
            for j in range(len(cole)):
                case.append(rowe[i][0] + cole[j][0] - rowe[i][1] -  cole[j][1])
            out.append(case)
        return out
#         for i in range(len_row):
#                 eachr = []
#                 for j in range(len_cols):
#                     eachr.append(rows[i] + cols[j]- (len_cols - rows[i]) - (len_row -  cols[j]))
#                 out.append(eachr)
#         return(out)
                    
                                   