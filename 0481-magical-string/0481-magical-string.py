class Solution:
    def magicalString(self, n: int) -> int:
        
        s = "122"
        for i in range(2,n):
            if s[-1]=="2":
                s+= "1"*int(s[i])
            else:
                s+= "2"*int(s[i])
            
        return s[:n].count("1")