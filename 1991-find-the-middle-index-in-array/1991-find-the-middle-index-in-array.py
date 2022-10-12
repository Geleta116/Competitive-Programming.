class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre = [0]
        for a in range(len(nums)):
            pre.append(nums[a]+pre[a])        
        pre= pre[1::]
        post = [0]*(len(nums)+1)
        for w in range(len(nums)-1,-1,-1):
            post[w]=post[w+1]+nums[w]
        post =  post[0:len(post)-1:1]
        out = 0
        print(pre)
        print(post)
        for i in range(len(pre)):
            if pre[i]==post[i]:
                return i
            
        return -1
        