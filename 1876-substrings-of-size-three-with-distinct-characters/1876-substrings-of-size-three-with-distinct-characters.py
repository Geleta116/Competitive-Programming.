class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        o = 0
        j = 2
        i= 0
        while j<len(s):
            c = list(set(s[i:j+1]))
            if len(c)==j-i+1:
                o+=1
            i+=1
            j+=1
        return o
        