class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)
            
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    found = dfs(neighbour)
                    if found:
                        return True
            return False
                    
            
        visited = set()
        self.graph = defaultdict(list)
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        return dfs(source)
        
        