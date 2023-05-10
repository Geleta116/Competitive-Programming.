class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        output = [[] for _ in range(n)]
        
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[1]].append(edge[0])
            
        def bfs(node, current, visited):
            queue = deque()
            queue.append(node)
            visited.add(node)
            
            while queue:
                
                curr = queue.popleft()
                if current != curr:
                    output[current].append(curr)
                
                for child in graph[curr]:
                    if child not in visited:
                        queue.append(child)
                        visited.add(child)
                        
        for i in range(n):
            bfs(i,i,set())
            
        for item in output:
            item.sort()
            
        return output
                
            
            