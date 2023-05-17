class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = [i for i in range(len(edges) + 2)]
        size = [1  for _ in range( len(edges) + 1)]
        graph = defaultdict(list)
        def bfs(node, val):
            queue = deque()
            queue.append(node)
            visited = set()
            visited.add(node)
            
            while queue:
                curr = queue.popleft()
                rep[curr] = val
                
                for child in graph[curr]:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
        
        for edge in edges:
            
            if rep[edge[0]] != rep[edge[1]]:
                
                if size[rep[edge[0]]] >= size[rep[edge[1]]]:
                    
                    size[rep[edge[0]]] += size[rep[edge[1]]]
                    store = rep[edge[0]]
                    bfs(edge[1], store)
                    graph[edge[0]].append(edge[1])
                    graph[edge[1]].append(edge[0])
                    
                    
                    
                else:
                    
                    size[rep[edge[1]]] += size[rep[edge[0]]]
                    store = rep[edge[1]]
                    bfs(edge[0], store)
                    graph[edge[1]].append(edge[0])
                    graph[edge[0]].append(edge[1])
            else:
                return [edge[0], edge[1]]
        