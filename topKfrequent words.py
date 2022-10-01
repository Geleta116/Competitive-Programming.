class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
            ct = Counter(words)
            new_heap = [(count,word) for word,count in ct.items()]
            new_heap = [(-count,word) for count,word in new_heap]
            heapq.heapify(new_heap)
            ans = []
            for i in range(k):
                ans.append(heapq.heappop(new_heap))
            ans = [(k) for j,k in ans]
            return ans
           
        
