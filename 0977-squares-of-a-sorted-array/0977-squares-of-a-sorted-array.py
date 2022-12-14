import heapq
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq = [i**2 for i in nums]
        heapq.heapify(sq)
        out = []
        while len(sq)!=0:
            out.append(heapq.heappop(sq))
        return out
            
        