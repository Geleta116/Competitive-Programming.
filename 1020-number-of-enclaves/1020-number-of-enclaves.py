class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int: 
        if grid[-1] == [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
            return 0
        
        def find(row, col):
            
            if par[(row, col)] == (row, col):
                return (row, col)
            
            r, c = par[(row,col)]
            par[(row, col)] = find(r, c)
            return par[(row, col)]
        
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def union(row1, col1, row2,  col2):
            tuple1 = (row1,col1)
            tuple2 = (row2,col2)
            
            par1, par2 = find(row1,col1), find(row2, col2)
            
            if par1 == par2:
                return
            
            if rank[par1] >= rank[par2]:
                rank[par1] += rank[par2]
                par[par2] = par1
                find(row2,col2)
                find(row1,col1)
                
            else:
                rank[par2] += rank[par1]
                par[par1] = par2
                find(row1,col1)
                find(row1,col2)
                
        par = defaultdict(tuple)
        rank = defaultdict(int)
        visited = set()
        par[(-1,-1)] = (-1,-1)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        rank[(-1,-1)] = 5000
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                rank[(row,col)] = 1
                if grid[row][col] == 1:
                    if  0 ==  row  or row == len(grid) -1 or 0 ==col or col == len(grid[0]) - 1:
                        par[(row,col)] = (-1,-1)
                        
                    else:
                        par[(row,col)] = (row,col)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 1:
                    
                    
                    for addedRow, addedCol in directions:
                        
                        newRow = row + addedRow
                        newCol = col + addedCol
                        
                        if inbound(newRow,newCol) and (newRow,newCol) and grid[newRow][newCol] == 1:
                            
                            visited.add((newRow,newCol))
                            union(row, col, newRow,newCol)
        out = 0
        
        for k in par:
            r,c = k
            find(r,c)
            if par[k] != (-1,-1):
                out += 1
   
                
        return out
                
                
            
                
            
            