class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
            if s[-1]=="1":
                return False
            pre = [0]*len(s)
            for i in range(len(s)):
                if i>0:
                    pre[i] +=pre[i-1]
                if  s[i]=='0' and (i == 0  or pre[i]>0):
                    if i+minJump<len(s):
                        pre[i+minJump] +=1
                    if i+maxJump+1<len(s):
                        pre[i+maxJump+1]-=1
            return pre[len(s)-1]>0
                    
                    
        