class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        t = n
        n = str(n)
        nums = []
        for l in n:
            nums.append(l)
        if len(nums)==1:
            return -1
        
        check = True
        for k in range(1,len(nums)):
            if nums[k-1]>=nums[k]:
                check = True
            else:
                check = False 
                break
        if check == True:
            return -1
        else:
            j = len(nums)-1
            while j>0:
                if nums[j]>nums[j-1]:
                    break
                else:
                    j-=1
            st = j
            j = j-1
            i = len(nums)-1
            while nums[i]<=nums[j]:
                    i-=1
            nums[i],nums[j] = nums[j],nums[i]
            nums[st::]= sorted(nums[st::])

            a = int("".join(nums))
            if a>int(n):
                if a < 1<<31:
                    return a  
                else :
                    return -1
            else:
                return -1




