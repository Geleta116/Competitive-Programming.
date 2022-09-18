class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        p =[0]
        for i in range(len(nums)):
            p.append(p[i]+nums[i])
        last = []
        n=0
        while n <len(p)-1:
            q = []
            q.append(p[n])
            q.append(nums[n])
            q.append(p[-1]-p[n]-nums[n])
            last.append(q)
            n+=1
        for j in range(len(last)):
            if last[j][0]==last[j][2]:
                return j
        return -1
        
