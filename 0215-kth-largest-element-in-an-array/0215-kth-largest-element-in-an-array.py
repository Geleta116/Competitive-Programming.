class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return min(heapq.nlargest(k,nums))
    
        