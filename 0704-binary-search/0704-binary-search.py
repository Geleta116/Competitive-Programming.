class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = len(nums)//2
        while left < right:
            mid = right - left + 1
            mid  = left + mid//2
            # print(mid)
            if nums[mid] > target :
                right = mid - 1
            elif nums[mid] < target:
                left = mid
            else:
                return mid
            
            
        if nums[left] ==  target:
            return left
        return -1
    
    
    
    
    
    
    
    
    
    
    
    
    
    