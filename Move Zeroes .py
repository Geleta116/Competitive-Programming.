class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
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
        """
        Do not return anything, modify nums in-place instead.
        """
