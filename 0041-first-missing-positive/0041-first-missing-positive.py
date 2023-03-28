class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for index in range(len(nums)):
            while nums[index] != index + 1 and nums[index] > 0 and nums[index] < len(nums) + 1:
                current = nums[index]
                if nums[current - 1] != current :
                    nums[index] , nums[current - 1] = nums[current - 1], nums[index]
                else:
                    break
        
        for index in range(len(nums)):
            if nums[index] != index + 1 :
                return index + 1
            
        return len(nums) + 1
                    
        