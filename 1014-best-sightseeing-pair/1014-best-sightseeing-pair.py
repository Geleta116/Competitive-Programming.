class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        running_sum = 0
        output = 0
        
        for item in values:
           
            output = max(output, running_sum + item)
            running_sum = max(running_sum, item) - 1
        
        return output