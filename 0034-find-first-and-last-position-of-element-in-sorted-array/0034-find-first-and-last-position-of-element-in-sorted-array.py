class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = -1
        right = len(nums)
        out = []
        if len(nums) == 0:
            return [-1, -1]
        def validate(n):
            if nums[n] >= target:
                return True
            return False
        
        def validate2(n):
            if nums[n] <= target:
                return True
            return False
            
        while right >  left + 1:
            mid = left + (right - left) // 2
            if validate(mid):
                right = mid
            else:
                left = mid
        
        right1 = right
        left = -1
        right = len(nums)
        
        while right >  left + 1:
            mid = left + (right - left) // 2
            if validate2(mid):
                left = mid
            else:
                right = mid
        
        if right1 < len(nums) and left < len(nums) and nums[right1] ==  target and nums[left] == target:
            return [right1, left]
        else:
            return [-1,-1]
        
        
        
        
        