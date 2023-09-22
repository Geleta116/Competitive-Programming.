class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0, float("-inf"))
        nums.append(float("-inf"))
        
        left = 1
        right = len(nums) - 2
        
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid - 1
            if nums[mid + 1] >= nums[mid]:
                left = mid + 1
            else:
                right  = mid - 1
        return (left + (right - left) // 2 ) - 1
        
        
        
        