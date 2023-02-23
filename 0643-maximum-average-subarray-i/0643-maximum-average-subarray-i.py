class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float("-inf")
        cur_sum = 0
        left = 0
        for right in range(len(nums)):
            if right - left + 1 < k:
                cur_sum += nums[right]
            else:
                cur_sum += nums[right]
                max_sum = max(max_sum , cur_sum)
                cur_sum -= nums[left]
                left += 1
        return max_sum/k
                
        
        
                
                
        
                
            
            
        