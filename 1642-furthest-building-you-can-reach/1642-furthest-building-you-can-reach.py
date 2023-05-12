class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        arr = []
        heapq.heapify(arr)
        
        for height in range(1,len(heights) ):
            #print(arr, height)
            if heights[height] > heights[height - 1] :
                
                    if ladders > 0:

                        ladders -= 1
                        heapq.heappush(arr, heights[height] - heights[height - 1])

                    elif bricks > 0:

                        diff = heights[height] - heights[height - 1]
                        
                        if arr and arr[0] <= diff:

                            current = heapq.heappop(arr)
                            heapq.heappush(arr, diff)
                            
                            if current > bricks:
                                return height - 1

                            else:
                                bricks -= current

                        elif bricks >= diff:

                            bricks -= diff
                        else:
                            return height - 1

                    else:
                        return height - 1
        
        return len(heights) - 1
                        
                    
                    
            
        