class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for read in range(len(nums)):
            while nums[read] != read + 1:
                if nums[read] == 0:
                    break
                else:
                    current = nums[read]
                    nums[read], nums[current - 1] = nums[current - 1], nums[read]
        if 0 in nums:  
            return nums.index(0) + 1
        else:
            return 0
                
        
        
        
        
        
        