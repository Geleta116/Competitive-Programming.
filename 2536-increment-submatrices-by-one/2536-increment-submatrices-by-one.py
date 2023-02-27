class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        grid = [[0 for _ in range(n)]for _ in range(n)]
        
        for query in queries:
            for row in range(query[0], query[2]+1):
                grid[row][query[1]] += 1
                if query[3]+1 < len(grid[0]):
                    grid[row][query[3]+1] -= 1
        
        
        for row in range(n):
            for col in range(1,n):
                grid[row][col] += grid[row][col - 1]
        
        return grid
        