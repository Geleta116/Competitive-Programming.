class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [-i for i in nums]
        
        y = heapq.nlargest(k, nums)
        y.sort()
        return y[0]
    
        