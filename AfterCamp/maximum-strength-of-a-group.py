class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        
        nums.sort()
        
        zeros_idx = bisect_right(nums, 0)
        
        negative = float("inf")
        left = 0
        right = 1
        
        if right < len(nums) and nums[right] < 0:
            negative = 1
            
            while right < len(nums) and nums[right] < 0:
                negative *= (nums[left] * nums[right])
                left += 2
                right += 2
          
        if len(nums) - zeros_idx != 0:
            if negative == float("inf"):
                negative = 1
                
            for number in nums[zeros_idx:]:
                negative *= number
        
        if negative == float("inf"):
            return max(nums)
        
        return negative
        
        
       
                