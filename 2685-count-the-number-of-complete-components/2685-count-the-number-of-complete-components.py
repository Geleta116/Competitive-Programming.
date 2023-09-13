class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # data structures
        self.graph = defaultdict(list)
        self.visited = set()
        self.queue = deque()
        compCount = 0
        
        # building the graph
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        
        
        #bfs implementation
        def bfs(node):
            self.queue.append(node)
            self.visited.add(node)
            nodeCount = 0
            edgeCount = 0
            while self.queue:
                nodeCount += 1
                curr  = self.queue.popleft()
                for child in self.graph[curr]:
                    edgeCount += 1
                    if child not in self.visited:
                        
                        self.queue.append(child)
                        self.visited.add(child)
         
            
            return nodeCount * (nodeCount - 1) == 2 * edgeCount // 2

            
            
        for vertice in range(n):
            if vertice not in self.visited:
                isComplete = bfs(vertice)
                if isComplete:
                    compCount += 1
                
        return compCount