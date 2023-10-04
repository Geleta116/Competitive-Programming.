import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = set()
        graph = defaultdict(list)
        heap =[(0,src, 0)]
        heapq.heapify(heap)
        for start, dest, weight in flights:
            graph[start].append((dest, weight))
        
        while heap:
            currCost, currNode, stops = heapq.heappop(heap)
            if (currNode,stops) in visited:
                continue
                
            visited.add((currNode,stops))
            
            if currNode ==  dst:
                return currCost
            
            if stops <= k:
                for child,cost in graph[currNode]:
                        heapq.heappush(heap, (currCost + cost, child, stops + 1))
        return -1
    
    
    