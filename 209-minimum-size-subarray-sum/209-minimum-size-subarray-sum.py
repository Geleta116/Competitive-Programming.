class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tot = 0
        for l in nums:
            tot+=l
        
        if tot < target:
            return 0
        elif tot == target:
            return len(nums)
        else:
            maxi  = max(nums)
            if maxi>= target:
                return 1
            else:
                out = len(nums)
                i = 0
                out = len(nums)
                summ = 0
                for j in range(len(nums)):
                    summ+=nums[j]
                    while summ>=target:
                        out = min(out,j-i+1)
                        summ-=nums[i]
                        i+=1
                return out
                
                
                

            