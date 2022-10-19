class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s1 = []
        i = 0
        while i<len(s):
            if s1 and  s1[-1][0]==s[i]:
                    s1[-1][1]=s1[-1][1]+1
            else:
                s1.append([s[i],1])
            if s1[-1][1]==k:
                s1.pop()
            i+=1
        out = ""
        for c,co in s1:
                out+=c*co
        return out
                
        
                
                
                
           