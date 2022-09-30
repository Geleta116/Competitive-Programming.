class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        count = 0
        while count<k:
            popped = heapq.heappop(nums)
            count+=1
        return -popped
        
