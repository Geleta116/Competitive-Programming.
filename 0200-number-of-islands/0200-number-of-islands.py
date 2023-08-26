class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # return 6
        rank = defaultdict(lambda : 1)
        par = defaultdict(tuple)
        out = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    par[(row,col)] = (row, col)
                    
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def find(row, col):
            
            if par[(row, col)] == (row, col):
                return (row, col)
            
            r, c = par[(row,col)]
            par[(row, col)] = find(r, c)
            return par[(row, col)]

        
        def union(r1, c1, r2, c2):
            par1, par2 = find(r1,c1), find(r2, c2)
            if par1 == par2:
                return
            if rank[par1] >= rank[par2]:
                rank[par1] += rank[par2]
                par[par2] = par1
                find(r2,c2)
                find(r1,c1)
                
            else:
                rank[par2] += rank[par1]
                par[par1] = par2
                find(r1,c1)
                find(r2,c2)
                                 
            
        def inbound(r, c):
            return 0 <= r < len(grid) and 0<= c < len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == "1":
                    for addedRow, addedCol in directions:
                        newRow = row + addedRow
                        newCol = col + addedCol
                        if inbound(newRow, newCol) and grid[newRow][newCol] == "1":
                            union(row, col, newRow, newCol)
        # print(par)
        for key in par:
            a, b = key
            find(a,b)
            out.add(par[key])
        return len(out)
                    
                                   
        
        
        
                                  
                                   