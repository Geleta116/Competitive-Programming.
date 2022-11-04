class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        p = [nums[0]]
        for i in range(1,len(nums)):
            p.append(p[-1]+nums[i])
        print(p)
        l = []
        out = -1
        nums.reverse()
        l = [nums[0]]
        for i in range(1,len(nums)):
            l.append(l[-1]+nums[i])
        a = 0
        l.reverse()
        while a<len(p):
            if l[a]==p[a]:
                return a
            else:
                a+=1
        return -1
            
        
            
            
        