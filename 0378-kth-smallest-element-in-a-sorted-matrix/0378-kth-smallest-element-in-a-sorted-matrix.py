class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr= []
        heapq.heapify(arr)
        
        for row in range(len(matrix)):
            for item in matrix[row]:
                heapq.heappush(arr, item)
        
        while k > 0:
            curr = heapq.heappop(arr)
            k -= 1
        
        return curr
        
        
        
        
        
        