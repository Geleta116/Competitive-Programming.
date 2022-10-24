class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1]=="1":
            return False
        n = len(s)
        psum = [0] * n
        for i in range(n):
            
            if i > 0:
                psum[i] += psum[i - 1]
            if s[i] == '0' and (i == 0 or psum[i] > 0):
                if i +minJump < n:
                    psum[i + minJump] += 1;
                if i + maxJump + 1 < n:
                    psum[i + maxJump + 1] -= 1
        return psum[n - 1] > 0
        