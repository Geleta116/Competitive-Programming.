class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
            else:
                continue
        i = 0
        while i<len(nums)-1:
            j = i+1
            while j<len(nums):
                if nums[i] == 0 and nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j+=1
                else:
                    j+=1
            i+=1
            
        return nums
            
        