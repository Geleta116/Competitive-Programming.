class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            if nums[0] != 0:
                return len(nums)
            return 1
        elif len(nums) == 2:
            if nums[0] - nums[1] == 0:
                return 1
            return 2
        
        turn = 0
        up = 1
        down = 1
        
        for index in range(1,len(nums)):
            if nums[index] - nums[index - 1] > 0 :
                up = down + 1
               
            elif nums[index] - nums[index - 1] < 0 :
                down = up + 1
               
                    
        return max(up, down) 
                    
                