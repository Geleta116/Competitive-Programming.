class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles = [-pile for pile in piles]
        
        heapq.heapify(piles)
        
        while k > 0:
            current = heapq.heappop(piles)
            current //= 2
            heapq.heappush(piles, current)
            k -= 1
            
        summ = 0
        for item in piles:
            summ += -item
            
        return summ
        