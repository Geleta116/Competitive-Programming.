class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        write = 0
        read = 0
        
        while read < len(nums):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            read += 1
                
        return nums
        
                