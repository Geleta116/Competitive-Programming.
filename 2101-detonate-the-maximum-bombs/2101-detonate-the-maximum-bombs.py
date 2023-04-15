class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def distance(startx, starty, endx, endy):
            return ((endx - startx) ** 2 + (endy - starty) ** 2) ** 0.5
        
        
        adjecency_list = defaultdict(list)
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    bombdist = distance(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1]) 
                    if bombdist <= bombs[i][2]:
                        adjecency_list[i].append(j)
                    
                    
                    
        self.max = 1
        self.visited = set()
      
        
        def dfs(node):
            for child in adjecency_list[node]:
                if child not in self.visited:
                    self.visited.add(child)
                    dfs(child)
        
        i = 0
        
        while i < len(bombs):
            self.visited = set([i])
            dfs(i)
            self.max = max(self.max, len(self.visited))
            i += 1
        
        return self.max
            
            
        
          
#         print(adjecency_list)
#         return 3
# #         self.max_length = 0
# #         visited = set()
        
# #         def dfs( node, visited, valid ):
        
# #             if len( visited ) == len(bombs):
# #                 return 
            
# #             visited.add(node)
# #             border = distance(node[0], node[1], child[0], child[1]) 
# #             bombDist = distance(node[0],node[1], node2[0], node2[1])
# #             if bombDist <= border:
# #                 valid.add
            
# #             if validation:
# #                 valid.add(node)
                
# #             for child in adjecency_list[node]:
                
# #                 if child not in visited and validation:
# #                     dfs(child,visited, valid)
                    
# #             self.max_length = max(self.max_length, len(valid))
        
# #         dfs(bombs, set(), set())
# #         return self.max_length
                    
                
            
            
        