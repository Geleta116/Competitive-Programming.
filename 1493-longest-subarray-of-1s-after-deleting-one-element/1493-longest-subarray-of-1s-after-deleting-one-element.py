class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        end = 0
        count = 0
        out = 0
        
        if nums[0]==0:
            count+=1
        if nums[0]==1:
            out = 1
        while end<len(nums)-1:
            if  count<=1:
                end+=1
                if nums[end]==0:
                    count+=1
                else:
                    out = max(out,end-start)
                
            elif count>1:
                while count>1 and start<=end:
                    if nums[start]==0:
                        count-=1
                        
                    start+=1
        return out
                    
                    
            
                
        