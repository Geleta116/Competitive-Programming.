class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        path = [0 for _ in range(10003)]
       
        for trip in trips:
            path[trip[1]] += trip[0]
            if trip[2]+1 < len(path):
                path[trip[2]] -= trip[0]
        
        for location in range(1,len(path)):
            path[location] += path[location - 1]
        
        for location in range(0,len(path)):
            if path[location] > capacity:
                return False
        
        return True
            
        