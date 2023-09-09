class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        # Data structures we use
        graph = defaultdict(list)
        self.maxi = 1
        # building the graph
        for index in range(len(parent)):
            if parent[index] == -1:
                continue
            graph[(parent[index], s[parent[index]])].append((index, s[index]))
        
        # dfs
        def dfs(node):
            
            if not node:
                return (0, "#")
            index, char = node
            running = 1
            out = []
            for child in graph[node]:
                max_leng, childChar = dfs(child)
                self.maxi = max(self.maxi, max_leng)
                if char != childChar:
                    out.append(max_leng)
            out.sort()
            if len(out) >= 2:
                running += out[-1]
                running += out[-2]
            elif len(out) == 1:
                running += out[-1]
            self.maxi = max(self.maxi, running)
            if out:
                return( out[-1] + 1, char)
            return(1, char)
        
        dfs((0,s[0]))
        return self.maxi
            
            
                                
            