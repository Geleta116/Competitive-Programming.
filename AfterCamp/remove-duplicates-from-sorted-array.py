class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left = 0
        right = 1
        
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left + 1], nums[right] = nums[right], nums[left + 1]
                right += 1
                left += 1
        return left + 1
        