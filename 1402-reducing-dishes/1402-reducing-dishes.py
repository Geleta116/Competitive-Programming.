class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        @cache
        def backtrack(index, mult):
            if index >= len(satisfaction):
                return 0
            
            left = backtrack(index + 1, mult)
            right = backtrack(index + 1, mult + 1) + satisfaction[index]*mult
            
            return max(right, left)
        
        return backtrack(0,1)
    
