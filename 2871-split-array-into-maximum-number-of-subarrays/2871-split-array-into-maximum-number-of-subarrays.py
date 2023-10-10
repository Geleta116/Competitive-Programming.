class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
       
        
        temp = nums[:]
        for i in range(1, len(nums)):
            temp[i] = temp[i - 1] and temp[i]
            
        # if temp[-1] != 0:
        #     return 1
        
        output = 0
        temp2 = nums[:]
        i = 0
        j = 0
        temp2.append(0)
        
        for i in range(len(nums)):
            
            if (temp2[i]) == 0 :
                output += 1
                     
            else:
                temp2[i + 1] = temp2[i + 1]  & temp2[i]
        if output == 0:
            return 1
        return output 
            
        