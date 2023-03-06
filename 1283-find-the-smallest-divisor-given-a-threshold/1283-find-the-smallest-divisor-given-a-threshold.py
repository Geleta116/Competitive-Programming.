class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def validate(n):
            run = 0
            for item in nums:
                if n == 0:
                    break
                run += math.ceil(item / n)
            if run <= threshold:
                return [True,run]
            return [False,run]
        
        
        left =  0
        right = max(nums) + 1
        
        
        while right > left + 1:
            mid = left + (right - left) // 2
            if validate(mid)[0] == True:
                store = validate(mid)[1]
                right = mid
            else:
                left = mid
        return right
            
        
        
        
        
        