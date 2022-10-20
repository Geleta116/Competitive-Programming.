class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = []
        heapq.heapify(nums)
        for c in range(len(nums)):
            l.append(heapq.heappop(nums))
        return l
            
        