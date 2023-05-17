class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        self.visited = set()
        self.output = 0
        def dfs(node):

            hasChild = False
            
            for child in graph[node] :
                if child not in self.visited:
                    self.visited.add(child)
                    childBool =  dfs(child)
                    if childBool == True:
                        hasChild = True
                        self.output += 2
            
            if hasApple[node] or hasChild:
                return True
            
            return False
        self.visited.add(0)
        dfs(0)
        return self.output
    