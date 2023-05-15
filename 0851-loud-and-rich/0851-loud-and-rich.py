class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        indegree = [0 for _ in range(len(quiet))]
        
        output = [ i  for i in range(len(quiet)) ]
        
        graph = defaultdict(list)
        
        for item in richer:
            graph[item[0]].append(item[1])
            indegree[item[1]] += 1

        queue = deque()
        
        for index in range(len(indegree)):
            if indegree[index] == 0:
                queue.append(index)
        
        while queue:
            
            curr = queue.popleft()
            
            for child in graph[curr]:
                if quiet[output[child]] > quiet[output[curr]]:
                    
                    output[child] = output[curr]
                
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
            
                    
        return output
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def bfs(node):
            
#             queu = deque()
#             queu.append(node)
#             small = node
            
#             while queu:
                
#                 curr = queu.popleft()
                
#                 if quiet[node] < quiet[curr]:
#                     quiet[curr] = quiet[node]
#                     self.quiteArr[curr] = node
                
#                 for child in graph[curr]:
#                     indegree[child] -= 1
#                     if indegree[child] == 0:
#                         self.queue.append(child)
#                     queu.append(child)
        
        
        
        # for index in range(len(indegree)):
        #     if indegree[index] == 0:
        #         self.queue.append(index)
               
#         while self.queue:
#             current = self.queue.popleft()
#             bfs(current)
            
            
#         print(quiet)
#         return self.quiteArr
                
        