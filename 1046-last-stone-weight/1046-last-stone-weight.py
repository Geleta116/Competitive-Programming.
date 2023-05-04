class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-value for value in stones]
        heapq.heapify(stones)
        
        while len(stones) >= 2:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first == second:
                continue
            else:
                second = first -  second
                heapq.heappush(stones, -second)
                
        if len(stones) == 1:
            return -stones[0]
        return 0
                
            
