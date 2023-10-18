class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # data strucuture definitions
        self.par =defaultdict(tuple)
        self.rank = defaultdict(int)
        
        # here we are gonna do the ranking
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                self.rank[(r,c)] = 1
                self.par[(r,c)] = (r,c)
                   
        def find(tupled):
            x,y = tupled
            if self.par[tupled] != tupled:
                self.par[tupled] = find(self.par[tupled])
            return self.par[tupled]
        
        def union(tupled1, tupled2):
            x1,y1 = tupled1
            x2,y2 = tupled2
            par_child1 = find(tupled1)
            par_child2 = find(tupled2)
            
            if par_child1 == par_child2:
                return
            
            if self.rank[par_child1] >= self.rank[par_child2]:
                self.rank[par_child1] += self.rank[par_child2]
                self.par[par_child2] = par_child1
                find(tupled2)
            
            else:
                self.rank[par_child2] += self.rank[par_child1]
                self.par[par_child1] = par_child2
                find(tupled1)
            return self.par[par_child1]
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def inbound(x,y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 1:
                    for addedRow, addedCol in directions:
                        newRow = row + addedRow
                        newCol = col + addedCol
                        
                        if inbound(newRow, newCol) and grid[newRow][newCol] == 1:
                            union((row, col), (newRow, newCol))
                            
        maxi = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                find((row,col))
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                curr = 0
                hasBeenAdded = set()
                if grid[row][col] == 0:
                    
                    for addedRow, addedCol in directions:
                        newRow = row + addedRow
                        newCol = col + addedCol
                        
                        if inbound(newRow, newCol) and grid[newRow][newCol] == 1:
                            if self.par[(newRow, newCol)] not in hasBeenAdded:
                                hasBeenAdded.add(self.par[(newRow, newCol)])
                                curr += self.rank[self.par[(newRow, newCol)]]
                maxi = max(maxi, curr + 1)
        if maxi == 1:
            if grid[0][0] == 1:
                
                return len(grid) * len(grid[0])
        
        return maxi
                        
                            
                    
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        