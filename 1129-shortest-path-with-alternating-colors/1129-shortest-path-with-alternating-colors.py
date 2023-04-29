class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], greenEdges: List[List[int]]) -> List[int]:
        redGraph = defaultdict(list)
        for item in redEdges:
            redGraph[item[0]].append(item[1])
            
        greenGraph = defaultdict(list)
        for item in greenEdges:
            greenGraph[item[0]].append(item[1])
        
        output = [float("inf")] * n
        queue = deque()
        queue.append((0, 1 , 0))
        # 0 means red and 1 means blue
        queue.append((0, 0 , 0))
        self.visited = set()
        self.visited.add((0,0))
        self.visited.add((0,1))
        
        while queue:
            current, color, level = queue.popleft()
            output[current] = min(output[current], level)
            alternate = 1 - color
            
            if alternate == 0:
                for child in redGraph[current]:
                    
                    if (child, alternate) not in self.visited:
                        self.visited.add((child, alternate))
                        queue.append((child, alternate, level + 1))
            else:
                for child in greenGraph[current]:
                    if (child, alternate) not in self.visited:
                        self.visited.add((child, alternate))
                        queue.append((child, alternate, level + 1))
        for i in range(len(output)):
            if output[i] == float("inf"):
                output[i] = -1
        return output
                
            
            