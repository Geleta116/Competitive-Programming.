class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        read = 0
        
        while read < len(nums) and write <= read:
            if nums[read] == 0:
                read += 1
                
            else:
                if nums[write] == 0:
                    nums[read], nums[write] = nums[write], nums[read]
                read += 1
                write += 1
                
                    
        """
        Do not return anything, modify nums in-place instead.
        """
        