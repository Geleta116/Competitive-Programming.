class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        check = True
        for k in range(1,len(nums)):
            if nums[k-1]>=nums[k]:
                check = True
            else:
                check = False 
                break
        if check == True:
            return nums.sort()
        else:
            j =len(nums)-1
            while j>0:
                if nums[j-1]<nums[j]:
                    break
                else:
                    j-=1
            st = j   
            j = j-1
            i = len(nums)-1
            while nums[j]>=nums[i]:
                i-=1
            nums[j],nums[i]= nums[i],nums[j]
            nums[j+1::]= sorted(nums[j+1::])
                    
            return nums
        
       
        
        """
        Do not return anything, modify nums in-place instead.
        """
        