class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        abs_min_1 = float("inf")
        abs_min_2 = float("inf")
        
        for item in nums:
            if item <= abs_min_1:
                abs_min_1 = item
            elif item <= abs_min_2:
                abs_min_2 = item
            else:
                return True
            
        return False
    