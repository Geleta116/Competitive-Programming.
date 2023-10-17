class Solution:
    def validateBinaryTreeNodes(self, n: int, left: List[int], right: List[int]) -> bool:
        self.par = defaultdict(int)
        self.rank = [1 for _ in range(n)]
        self.hasParent = set()
        for ids in range(n):
            self.par[ids] = ids
            
        def find(x):
            if self.par[x] != x:
                self.par[x] = find(self.par[x])
            return self.par[x]
        
        
        def union( x1, x2):
            par_x1, par_x2 = find(x1), find(x2)
            if par_x1 == par_x2:
                return False
            if self.rank[par_x1] >= self.rank[par_x2]:
                self.rank[par_x1] += self.rank[par_x2]
                self.par[par_x2] = par_x1
            else:
                self.rank[par_x2] += self.rank[par_x1]
                self.par[par_x1] = par_x2
            return True
        
        
        for idx in range(n):
            if left[idx] != -1:
                
                canBeUnioned = union(idx, left[idx])
                if not canBeUnioned or left[idx] in self.hasParent:
                    
                    return False
                self.hasParent.add(left[idx])
                
            if right[idx] != -1:
                canBeUnioned = union(idx, right[idx])
                if not canBeUnioned or right[idx] in self.hasParent:
                    return False
                self.hasParent.add(right[idx])
              
        for cl in self.par:
            find(cl)
          
        count = set()
        for key in self.par:
            count.add(self.par[key])
            
        if len(count) == 1:
            return True
        
        return False
        