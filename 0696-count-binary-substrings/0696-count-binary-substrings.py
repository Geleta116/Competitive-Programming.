class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = s.replace("10","1 0")
        s = s.replace("01","0 1")
        l = s.split(" ")
        out = []
        for i in l:
            out.append(len(i))
        ret = 0
        i = 0
        j =1
        while j<len(out):
            ret += min(out[j],out[i])
            i+=1
            j+=1
        return ret
    
    