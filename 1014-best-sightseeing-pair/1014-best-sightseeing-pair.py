class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        running_sum_minus_dist = 0
        output = 0
        
        for item in values:
           
            output = max(output, running_sum_minus_dist + item)
            running_sum_minus_dist = max(running_sum_minus_dist, item) - 1
        
        return output