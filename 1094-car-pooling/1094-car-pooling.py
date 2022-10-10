class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        activity = []
        for passenger,start,end in trips:
            activity.append([start,passenger])
            activity.append([end,-passenger])
        activity.sort()
        for loc,passs in activity:
            capacity -= passs
            if capacity<0:
                return False
        return True
        
        
        