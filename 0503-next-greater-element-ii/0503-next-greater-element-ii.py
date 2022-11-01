class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        out = [-1]*len(nums)
        s = []
        lnums = nums*2
        for i in range(len(lnums)):
            while s and s[-1][0]<lnums[i]:
                val,pos = s.pop()
                out[pos] = lnums[i]
            if i<len(nums):
                s.append(( lnums[i],i))
        return out
            
       