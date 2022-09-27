class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        pre = [0]
        for k in range(len(nums)):
            pre.append(pre[k]+nums[k])
        firstmax = 0
        res = 0
        for i in range(firstLen+1,len(pre)-secondLen+1):
            firstsum = pre[i+secondLen-1]-pre[i-1]
            firstmax = max(firstmax,pre[i-1]-pre[i-firstLen-1])
            res = max(res,firstsum+firstmax)
        secondmax = 0
        for i in range(secondLen+1,len(pre)-firstLen+1):
            secondsum = pre[i+firstLen-1]-pre[i-1]
            secondmax = max(secondmax,pre[i-1]-pre[i-secondLen-1])
            res = max(res,secondsum+secondmax)
        return res
        
        
