class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:      
        output = 0
        temp2 = nums[:]
        temp2.append(0)
        for i in range(len(nums)):
            if (temp2[i]) == 0 :
                output += 1     
            else:
                temp2[i + 1] = temp2[i + 1]  & temp2[i]
        if output == 0:
            return 1
        return output 
            
        