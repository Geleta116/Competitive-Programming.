class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        def inbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        
        directions = [(1,0) , (-1,0) , (0,1), (0,-1)]
        self.visited = [[False for i in range(len(image[0]))] for j in range(len(image))]
        print(self.visited)
        def dfs(row, col, originalColor):
            
            self.visited[row][col] = True
            image[row][col] = color
            for addedRow, addedCol in directions:
                newRow = row + addedRow
                newCol = col + addedCol
                
                if inbound(newRow, newCol) and (image[newRow][newCol] == originalColor) :
                    if not self.visited[newRow][newCol]:
                        dfs(newRow, newCol, originalColor)
        
        
        dfs(sr, sc, image[sr][sc])
        
        return image
            
            
            
        