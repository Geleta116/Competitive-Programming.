import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        visited = set()
        
        for source, dest, weight in times:
            graph[source].append((dest, weight))
        
        visited.add(k)
        heap = [(0,k)]
        heapq.heapify(heap)
        maxi = float("-inf")
        
        while heap:
            
            currCost, currNode =  heapq.heappop(heap)
            maxi =  max(currCost, maxi)
            visited.add(currNode)
            if len(visited) == n:
                return maxi
            
            for  childNode, childCost in graph[currNode]:
                
                if childNode not in visited:
                   
                    heapq.heappush(heap, (currCost + childCost, childNode))
            
        return -1
            
        