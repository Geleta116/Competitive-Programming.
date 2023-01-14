class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        i = 0
        j = 0
        while j<len(nums):
            if nums[j] == 1 and nums[i]==1:
                maxi = max(maxi, j-i+1)
                j+=1
            elif nums[j] == 0:
                i = j+1
                j+=1
        return maxi
                
        