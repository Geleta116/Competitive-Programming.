class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True
        else:
            c = 0
            i = 0
            j = 0
            while j<len(t) and i<len(s):
                if s[i]!=t[j]:
                    j+=1
                else:
                    i+=1
                    j+=1
                    c+=1
            return c == len(s)
            
        