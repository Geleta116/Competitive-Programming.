class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[0 for c in range(len(dungeon[0]))] for r in range(len(dungeon)) ]
        dp[len(dungeon) - 1][len(dungeon[0]) - 1] = dungeon[len(dungeon) - 1][len(dungeon[0]) - 1] if dungeon[len(dungeon) - 1][len(dungeon[0]) - 1] < 0 else 0
        
        for row in range(len(dungeon) - 1, -1,-1):
            for col in range(len(dungeon[0]) - 1, -1, -1):
                if row + 1 < len(dungeon):
                    bottom = dp[row + 1][col]
                    
                if col + 1 < len(dungeon[0]):
                    right = dp[row][col + 1]
                    
                if row + 1 < len(dungeon) and col + 1 < len(dungeon[0]):
                    if (max(right, bottom) + dungeon[row][col]) >=0:
                        dp[row][col] = 0 

                    else:
                        
                        dp[row][col] = max(right, bottom) + dungeon[row][col]
                elif row + 1 < len(dungeon):
                    if (bottom + dungeon[row][col]) >=0:
                        dp[row][col] = 0 

                    else:
                        
                        dp[row][col] = bottom + dungeon[row][col]
                elif col + 1 < len(dungeon[0]):
                    if (right + dungeon[row][col]) >=0:
                        dp[row][col] = 0 

                    else:
                        
                        dp[row][col] = right + dungeon[row][col]
                    
        print(dp)
        return  1 - dp[0][0] if dp[0][0] < 0 else 1
                
        
        