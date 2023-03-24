class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for read in range(len(nums)):
            while nums[read] != read + 1:
                current = nums[read]
                if nums[current - 1] == nums[read]:
                    break
                nums[read], nums[current - 1] = nums[current - 1], nums[read]
        
        for index, number in enumerate(nums):
            if index + 1 != number:
                return  number
                
        
        