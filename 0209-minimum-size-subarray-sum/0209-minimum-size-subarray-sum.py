class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_leng = float("inf")
        left = 0
        curr_sum = 0
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_leng = min(min_leng, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        if min_leng != float("inf"):
            return min_leng
        else:
            return 0
            
                
            
        
                
                
                

            