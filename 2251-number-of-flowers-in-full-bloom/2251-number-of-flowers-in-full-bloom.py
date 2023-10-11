class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        time = []
        heap= []
        heapq.heapify(heap)
        for idx, node in enumerate(people):
            time.append([node, idx])
        time.sort()
        out = [0 for _ in range(len(people))]
        flowerIdx = 0
        for arrival, index in time:
            while flowerIdx < len(flowers) and flowers[flowerIdx][0] <= arrival:
                heapq.heappush(heap, flowers[flowerIdx][1])
                flowerIdx += 1
            
            while heap and heap[0] < arrival:
                heapq.heappop(heap)
            out[index] = len(heap)
        return out
                
            