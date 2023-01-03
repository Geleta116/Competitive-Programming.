import numpy 
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        untransposed = grid
        transposed = numpy.transpose(grid)
        row_dict = defaultdict(int)
        col_dict = defaultdict(int)
        for rows in untransposed:
            row_dict[tuple(rows)]+=1
        for cols in transposed:
            col_dict[tuple(cols)] += 1
        for array in row_dict:
            if array in col_dict:
                count += row_dict[array]*col_dict[array]
        
            
           
        
        # for rows in untransposed:
        #     # stringify = [str(num) for num in rows]
        #     # stringy_rows = "".join(stringify)
        #     for columns in transposed:
        #         # stringify = [str(num) for num in columns]
        #         # stringy_cols = "".join(stringify)
        #         flag = True
        #         for item in range(len(columns)):
        #             if columns[item]!= rows[item]:
        #                 flag = False
        #         if flag:
        #                 count += 1
        return count
        