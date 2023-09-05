class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        queue = deque([(1, 0)])  # (current position, steps)
        visited = set()

        while queue:
            index, level = queue.popleft()
            visited.add(index)

            if index == target:
                return level

            for i in range(1, 7):
                next_index = index + i
                if next_index > target:
                    break

                row = n - 1 - (next_index - 1) // n
                col = (next_index - 1) % n if (n - row) % 2 == 1 else n - 1 - (next_index - 1) % n

                if board[row][col] != -1:
                    next_index = board[row][col]

                if next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, level + 1))

        return -1




                    
        
        
        
        
        
        
        
        
            
            
        