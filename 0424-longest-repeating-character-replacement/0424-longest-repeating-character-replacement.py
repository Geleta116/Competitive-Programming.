class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        out = 0
        c = {}
        while j<len(s):
            c[s[j]]= 1+c.get(s[j],0)
           
            while (j-i+1)- max(c.values()) > k:
    
                c[s[i]] -=1
                i+=1
            
            out = max(out,j-i+1)
            j+=1
                
                
                
        return out
            
        
        