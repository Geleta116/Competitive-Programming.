class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        par = defaultdict(int)
        rank = defaultdict(int)
        newQuery = [(cost, left, right, i) for i,(left, right, cost) in enumerate(queries) ]
        newQuery.sort()
        edgeList.sort(key= lambda x:x[2])
        print(newQuery)
        for num in range(n):
            par[num] = num
            rank[num] = 1
        
        def find(num):
            
            if par[num] != num:
                par[num] = find(par[num])
                
            return par[num]
        
        def union(num1, num2):
            par1, par2 = find(num1), find(num2)
            
            if par1 != par2:
                
                if rank[par1] >= rank[par2]:
                    rank[par1] += rank[par2]
                    par[par2] = par1
                    find(num2)
                    
                else:
                    rank[par2] += rank[par1]
                    par[par1] = par2
                    find(num1)
                    
        output = [False for _ in range(len(queries))]   
        start = 0
        
        for (cost, left, right, index) in newQuery:
           
            while start < len(edgeList) and edgeList[start][2] < cost:
                union(edgeList[start][0], edgeList[start][1])
                start += 1
                
            output[index] = find(left) == find(right)
            
        return output
        