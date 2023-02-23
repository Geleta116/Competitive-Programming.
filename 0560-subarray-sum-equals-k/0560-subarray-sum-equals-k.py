class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_out = 0
        running_sum = 0
        checker = defaultdict(int)
        for right in nums:
            running_sum += right
            if running_sum - k in checker:
                total_out += checker[running_sum - k]
            if running_sum == k:
                total_out += 1
            checker[running_sum] += 1
        return total_out
    
       
        
        
        