class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        visited.add(0)
        queue = deque()
        queue.append(0)
        
        while queue:
            current = queue.popleft()
            for room in rooms[current]:
                if room not in visited:
                    visited.add(room)
                    queue.append(room)
                    
        if len(visited) == len(rooms):
            return True
        return False
                
                