class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        out = 0
        p = {0:1}
        summ = 0
        for i in nums:
            summ +=i
            diff = summ-goal
            out+=p.get(diff,0)
            p[summ ]= 1+p.get(summ,0)
            
        return out
            
        
            