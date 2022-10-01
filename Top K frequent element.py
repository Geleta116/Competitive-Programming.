class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            ct = Counter(nums)
            new_heap = [(count,item) for item,count in ct.items()]
            new_heap = [(-count,item) for count,item in new_heap]
            heapq.heapify(new_heap)
            ans = []
            for i in range(k):
                ans.append(heapq.heappop(new_heap))
            ans = [(k) for j,k in ans]
            return ans
           
        
            
        
