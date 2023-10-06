import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # we are gonna use a heap and then insert into the heap -(probability) so that when we take the node with the most probability first
        graph = defaultdict(list)
        
        for idx in range(len(succProb)):
            graph[edges[idx][0]].append([-succProb[idx], edges[idx][1], ])
            graph[edges[idx][1]].append([-succProb[idx], edges[idx][0]])
        
        heap = []
        heapq.heapify(heap)
        
        for succ, node in graph[start_node]:
            heapq.heappush(heap, (succ,node))
        
        visited = set()
        
        while heap:
            currSucc, currNode =  heapq.heappop(heap)
            
            if currNode in visited:
                continue
            
            if currNode == end_node:
                return -currSucc
            
            visited.add(currNode)
            
            for childSucc, childNode in graph[currNode]:
                if childNode not in visited:
                    heapq.heappush(heap, (-(currSucc * childSucc), childNode))
        return 0
        
        
        
        