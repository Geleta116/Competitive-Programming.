class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        temp = k
        out = 0
        start = 0
        end = 0
        t = 0
        
        while temp>0 and end<len(s):
            if s[end]=="a"  or s[end]=="o"  or s[end]=="e" or s[end]=="i" or s[end]=="u":
                t+=1
                out = max(out,t)
            end+=1
            temp-=1
        end -=1
        while end<len(s):
            out = max(out,t)
            if end<len(s)-1:
                end+=1
                if s[end]=="a" or s[end]=="o" or s[end]=="u" or s[end]=="e" or s[end]=="i":
                    t+=1
                if s[start]=="a" or s[start]=="o" or s[start]=="u" or s[start]=="e" or s[start]=="i":
                    t-=1
                start+=1
            else:
                break
        return out