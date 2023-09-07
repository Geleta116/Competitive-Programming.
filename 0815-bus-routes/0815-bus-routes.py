class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        # Data structures
        
        graph = defaultdict(set)
        sec_graph = defaultdict(set)
        queue = deque()
        visited = set()
        
        # graph
        if source == target:
            return 0
        
        for index in range(len(routes)):
            for busStop in routes[index]:
                graph[busStop].add(index)
                
        # bfs
        for item in graph[source]:
            queue.append((item,1))
            visited.add(item)
        
        while queue:
            currPar, level = queue.popleft()
            
            if target in routes[currPar]:
                return level
            
            for child in routes[currPar]:
                for item in graph[child]:
                    if item not in visited:
                        visited.add(item)
                        queue.append((item, level + 1))
        return -1
                    
                