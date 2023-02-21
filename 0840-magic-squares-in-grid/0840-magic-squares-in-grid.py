class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])
        out = 0
        for rows in range(num_row-2):
            for cols in range(num_col-2):
                sum_first_row = 0
                
                # for a_cell in grid[rows,rows+3]:
                
                for each_col in range(cols, cols+3):
                    sum_first_row += grid[rows][each_col]
                
                   
                temp_set = set()
                z_box_is_magic = True
                for each_row in range(rows, rows+3):
                    temp = 0
                    for each_col in range(cols, cols+3):
                        if grid[each_row][each_col] in temp_set:
                            z_box_is_magic = False
                            break
                        elif grid[each_row][each_col] < 1 or grid[each_row][each_col] >9:
                            z_box_is_magic = False
                            break
                        else:
                            temp_set.add(grid[each_row][each_col])
                            temp += grid[each_row][each_col]
                            
                    if temp != sum_first_row:
                        z_box_is_magic = False
                        break
                    else:
                        continue
                if z_box_is_magic ==  False:
                    continue
                else:
                    for each_col in range(cols, cols+3):
                        temp = 0
                        for each_row in range(rows, rows+3):
                            temp += grid[each_row][each_col]
                        if temp != sum_first_row:
                            z_box_is_magic = False
                            break
                        else:
                            continue
                    if z_box_is_magic ==  False:
                        continue
                    else:
                        if grid[rows][cols]+ grid[rows+1][cols+1]+grid[rows+2][cols+2]!= sum_first_row or sum_first_row != grid[rows][cols+2]+ grid[rows+1][cols+1]+grid[rows+2][cols]:
                            z_box_is_magic = False
                        else:
                            out += 1
        return out
                            
                    
                        
                            
                        
                        
                        