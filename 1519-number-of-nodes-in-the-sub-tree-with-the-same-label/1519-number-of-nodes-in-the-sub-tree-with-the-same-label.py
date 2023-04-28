class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        
        for edge in edges:
            
            graph[(edge[0], labels[edge[0]])].append((edge[1], labels[edge[1]]))
            graph[(edge[1], labels[edge[1]])].append((edge[0], labels[edge[0]]))   
            
        self.out = [1 for i in range(len(labels))]
        self.visited = set()
        def dfs(root):
            store = defaultdict(int)
            if len(graph[root]) == 0:
                store[root[1]] += 1
                return store
            
            for child in graph[root]:
                if child not in self.visited:
                    self.visited.add(child)
                    current = dfs(child)
                    for item in current:
                        store[item] += current[item]
            
            self.out[root[0]] += store[root[1]]
            store[root[1]] += 1
            return store
        self.visited.add((0,labels[0]))
        dfs((0,labels[0]))
        
        return self.out