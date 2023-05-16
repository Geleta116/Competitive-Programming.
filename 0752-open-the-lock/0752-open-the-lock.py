class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        queue = deque()
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        queue.append("0000")
        def neighbors(code):
            for i in range(4):
                x = int(code[i])
                for diff in (-1, 1):
                    y = (x + diff + 10) % 10
                    yield code[:i] + str(y) + code[i + 1:]
        
        count = -1
        visited = set()
        visited.add("0000")
        while queue:
            
            count += 1
            
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return count
                
                for neigh in neighbors(curr):
                    if neigh not in deadends and neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)
            
            
        return -1
                
                
            
            
        