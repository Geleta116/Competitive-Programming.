class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]: 
        nums.sort()
        y = [None]*(len(nums))
        c = 0
        b = 0
        d= -1
        while c<len(nums):
            y[c] = nums[b]
            if c!=len(nums)-1:
                y[c+1]=nums[d]
            c+=2
            b+=1
            d-=1
        return(y)

    
    
    
