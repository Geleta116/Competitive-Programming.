class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        self.queue = deque()
        self.visited = set()
        self.queue.append((1,0))
        
      
        while self.queue:
            
            n_index, level = self.queue.popleft()         
            
            if n_index == n * n:
                
                return level
            
            for i in range(1,7):
                
                index = n_index + i
                
                if index > n * n:
                    break
                    
                row = n - 1 - (index - 1) // n
                
                column =  (index - 1) % n if (n - row) % 2 == 1 else n - 1 - (index - 1) % n

                if board[row][column] == -1 :

                        if index not in self.visited:

                            self.visited.add(index)
                            self.queue.append((index, level + 1))


                if board[row][column] != -1 :
                    if board[row][column] not in self.visited:
                        self.visited.add(board[row][column])
                        self.queue.append((board[row][column], level + 1))

        return -1
                    
   
        
        
        
        
            
            
        