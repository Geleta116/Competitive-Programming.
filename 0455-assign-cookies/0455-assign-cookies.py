class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        if len(s)==0:
            return 0
        if g[i]>s[-1]:
            return 0
        else:
            out = 0
            while i<len(g) and j<len(s):
                if g[i]<=s[j]:
                        out+=1
                        i+=1
                j+=1
               

            return out
            
            
        