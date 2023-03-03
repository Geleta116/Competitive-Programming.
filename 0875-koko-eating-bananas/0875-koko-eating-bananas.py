class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #This is the initialization of the left and the right pointers
        left = 0
        right = max(piles) + 4
        
        
        #This is the validate function
        def validate(piles,speed):
            total_hour = 0
            for banana in piles:
                hour =  banana / speed
                total_hour += ceil(hour)
            if total_hour <= h:
                return True
            return False
        
        
        #This is the binary search implementation
        while right > left + 1:
            mid = left + (right - left)//2
            if validate(piles,mid):
                right = mid
            else:
                left = mid
        return right
    
        
        