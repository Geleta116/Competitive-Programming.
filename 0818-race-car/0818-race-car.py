class Solution:
    def racecar(self, target: int) -> int:
        queue = deque()
        queue.append((0,1,0))
        
        while queue:
            pos, speed, num = queue.popleft()
            
            if pos == target:
                return num
            
            queue.append((pos + speed, speed * 2, num + 1))
            
           
            if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                queue.append((pos, -1 if speed > 0 else 1, num + 1))
                
        return -1