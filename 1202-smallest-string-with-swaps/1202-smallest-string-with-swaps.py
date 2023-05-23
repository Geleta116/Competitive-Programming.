class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = defaultdict(int)
        answer = list(s)
        for index in range(len(s)):
            
            parent[index] = index
        
        
        
        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            
            if par1 <= par2:
                parent[par2] = par1
            else:
                parent[par1] = par2
        
        
        
        def find(node):
            if parent[node] == node:
                return node
            
            par = find(parent[node])
            parent[node] = par
            return par
        
        
        
        for pair in pairs:
            union(pair[0], pair[1])
        
        groups = defaultdict(list)
        for key in parent:
            find(key)
        
        for key in parent:
            groups[parent[key]].append(key)
        
        
        
        for group in groups:
            store = []
            groups[group].sort()
            for item in groups[group]:
                store.append(s[item])
            store.sort()
            index = 0
            
            for item in groups[group]:
                answer[item] = store[index]
                index += 1
                
        return "".join(answer)
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        