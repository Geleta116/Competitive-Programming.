class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited = set()
        store = []
        heapq.heapify(store)
        output = []
        heapq.heappush(store, (nums1[0] + nums2[0], 0,0))
        
        while k > 0 and len(store) > 0:
            val, i, j = heapq.heappop(store)
            output.append([nums1[i], nums2[j]])
            
            if ((i,j + 1) not in visited) and j + 1 < len(nums2):
                heappush(store, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i,j + 1))
            
            if ((i + 1,j ) not in visited) and i + 1 < len(nums1):
                heappush(store, (nums1[i + 1] + nums2[j], i + 1, j ))
                visited.add((i + 1,j))
                
            k -= 1
                
        return output
            
        