class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if sum(values) == 0:
            return len(values)
        
        graph = defaultdict(list)
        
        for start, dest in edges:
            graph[start].append(dest)
            graph[dest].append(start)
        graph['a'] = [0]
        # print(graph)
        self.visited = set([0])
        
        def dfs(node):
            if node == 'a':
                dfs(0)
                return
            self.visited.add(node)
            if len(graph[node]) == 1 and node != 0:
                if values[node] % k == 0:
                    
                    return False
                
                return True
            
            for child in graph[node]:
                if child not in self.visited:
                    
                    store = dfs(child)
                    
                    if store:
                        values[node] += values[child]
                        values[child] = -1
                        
            if values[node]%k == 0:
                return False
            return True
                        
        tstore = dfs('a')
        # print(values)
        out = 0
        for i in values:
            if i != -1:
                out += 1
        
        return out
                        
            
                    
                    
        
        