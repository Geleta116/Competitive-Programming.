class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        self.paths = []
        adjecency_list = {}
        
        for index in range(len(graph)):
            adjecency_list[index] = graph[index]
        
        def dfs(currentNode, currentPath):
            
            if currentNode == len(graph) - 1 :
                self.paths.append(list(currentPath))
                return
            
            for child in adjecency_list[currentNode]:
                currentPath.append(child)
                dfs(child, currentPath)
                currentPath.pop()
                
            
        
        dfs(0,[0])
    
        return self.paths
                
        