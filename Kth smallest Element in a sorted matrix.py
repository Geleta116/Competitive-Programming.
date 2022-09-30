class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []
        for i in matrix:
            temp.extend(i)
        temp.sort()
        heapq.heapify(temp)
        count = 0
        while count<k:
            popped = heapq.heappop(temp)
            count+=1
        return popped
            
        
