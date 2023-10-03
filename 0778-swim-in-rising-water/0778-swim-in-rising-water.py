import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
    
        heap = [(grid[0][0], 0, 0)]
        heapq.heapify(heap)

        visited = set()

        while heap:

            currCost, r, c = heapq.heappop(heap)

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return currCost

            for addedRow, addedCol in directions:
                newRow =  r + addedRow
                newCol = c + addedCol 

                if inbound(newRow, newCol) and  (newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    if grid[newRow][newCol] <= currCost:

                        heapq.heappush(heap, (currCost, newRow, newCol))
                    else:
                        diff =  grid[newRow][newCol] - currCost
                        heapq.heappush(heap, (currCost + diff, newRow, newCol))
