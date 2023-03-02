class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        '''
        explanation:
        find the suffix for the first row
        find the prefix for the second row
        then at each point try to minimize the point where you pick the lowest and the highest
        the above line is due to the constraint applied by the first player
        then try to take maximum 
        
        time complexity: o(n)
        space complexity: o(n)
        '''
        
        #calculate the suffix for the first row
        #calculate the prefix for the second row
        
        suffix = [0 for num in range(len(grid[0]))]
        prefix = [0 for num in range(len(grid[1]))]
        
        # populate the suffix and the prefix for each row
        
        for index in range(len(grid[0])-2,-1,-1):
            suffix[index] = grid[0][index + 1] + suffix[index + 1]
                                        
        for index in range(1,len(prefix)):
            prefix[index] = grid[1][index - 1] + prefix[index - 1]
                            
        rob2_points = float("inf") #since the maximum value is lower than this
        for index in range(len(prefix)):
            rob2_points = min(rob2_points,max(suffix[index], prefix[index]))
            
        
        return rob2_points
            
        
        
        
        
        
        