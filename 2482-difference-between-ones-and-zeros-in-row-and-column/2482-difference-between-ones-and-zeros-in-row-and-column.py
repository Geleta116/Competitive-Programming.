class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        len_row = len(grid)
        len_cols = len(grid[0])
        
        rows = [0] * len_row
        cols = [0] * len_cols
        
        for row_item in range(len(rows)):
            for col_item in range(len(cols)):
                rows[row_item]+= grid[row_item][col_item]
                cols[col_item]+= grid[row_item][col_item]
     
        out = []
        rowe = []
        cole = []
        for row_item  in rows:
            case = [row_item, len_cols - row_item]
            rowe.append(case)
        for col_item in cols:
            case = [col_item, len_row - col_item]
            cole.append(case)
        
        for item in range(len(rowe)):
            new_row = []
            for cols in range(len(cole)):
                new_row.append(rowe[item][0] + cole[cols ][0] - rowe[item][1] -  cole[cols ][1])
            out.append(new_row)
        return out

                                   