class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = 0
        out = 0 
        tot = 0
        while j<len(nums):
            tot +=nums[j]
            while  nums[j]*(j-i + 1)>tot + k:
                tot-=nums[i]
                i += 1
            out = max(out,j-i+1)
            j+=1
            
        return out
                