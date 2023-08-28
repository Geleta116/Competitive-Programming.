class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        par = defaultdict(int)
        rank = defaultdict(lambda: 1)
        groups = defaultdict(list)
        
        for idx in range(len(source)):
            par[idx] = idx
        
        def find(idx):
            
            if par[idx] != idx:
                par[idx] = find(par[idx])
            
            return par[idx]
        
        def union(idx1, idx2):
            par1, par2 = find(idx1), find(idx2)

            if rank[par1] >= rank[par2]:
                par[par2] = par1
                rank[par1] += rank[par2]
            else:
                par[par1] = par2
                rank[par2] += rank[par1]
                
        for edge in allowedSwaps:
            union(edge[0], edge[1])
        
        ans = 0
        for key in par:
            find(key)
        
        
        for key in par:
            groups[par[key]].append(key)
        
        answer = 0
        for indexArray in groups.values():
            count = collections.Counter()
            for index in indexArray:
                count[source[index]] += 1
                count[target[index]] -= 1
            
            answer += sum(abs(value) for value in count.values())//2
        return answer
            
            
                
            
        