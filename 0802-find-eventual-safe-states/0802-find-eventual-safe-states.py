class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        colors = [0 for _ in range(len(graph))]
        
        def dfs(node):
            
            if  colors[node] == 1:
                return False
            
            colors[node] = 1
            
            for child in graph[node]:
                if colors[child] == 2:
                    continue
                
                store = dfs(child)
                if not store:
                    return False
            
            
            colors[node] = 2
            return True
            
            

        for node in range(len(graph)):
            if colors[node] != 0:
                continue
            else:
                dfs(node)
                
        
        
        output = []
       
        for item in range(len(colors)):
            
            if colors[item] == 2:
                output.append(item)
                
        return output
            
            
            
        