import heapq

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        graph = defaultdict(list)
        for idx , (source, destination) in enumerate(equations):
            graph[source].append((values[idx], destination))
            graph[destination].append((1/values[idx], source))
        
        out = []
        for qSource, qDestination in queries:
            queue = deque()
            queue.append((1, qSource))
            visited = set()
            found = False
            if qSource in graph and qDestination in graph:
                while queue:
                    currCost , currNode = queue.popleft()

                    if currNode in visited:
                        continue

                    visited.add(currNode)
                    if currNode == qDestination:
                        print(graph)
                        out.append(currCost)
                        queue = deque()
                        found= True

                    else:
                        for childCost, child in graph[currNode]:
                            queue.append((childCost*currCost, child))
                if not found:
                    out.append(-1)
            else:
                out.append(-1)
        # print(out)
        return out
                    
                    
                
            
        
        
        