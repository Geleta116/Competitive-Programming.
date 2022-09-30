import heapq as hq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        hq.heapify(stones)
        
        while len(stones)>1:
            popped1 = hq.heappop(stones)
            popped2 = hq.heappop(stones)
            if popped1 < popped2:
                hq.heappush(stones,popped1- popped2)
                
        stones.append(0)
        return -(stones[0])
        
        
