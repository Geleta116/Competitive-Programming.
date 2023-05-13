class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        inorder = defaultdict(int)
        
        for pairs in adjacentPairs:
            graph[pairs[0]].append(pairs[1])
            graph[pairs[1]].append(pairs[0])
            inorder[pairs[0]] += 1
            inorder[pairs[1]] += 1
        
        queue = deque()
        
        for edge in inorder:
            if inorder[edge] == 1:
                queue.append(edge)
        
        output = []
        self.visited = set()
        
        def dfs(node):
            if node in self.visited:
                return
            
            self.visited.add(node)
            output.append(node)
            
            for item in graph[node]:
                if item not in self.visited:
                    dfs(item)
                    
        dfs(queue.popleft())
        return output
            
        
                