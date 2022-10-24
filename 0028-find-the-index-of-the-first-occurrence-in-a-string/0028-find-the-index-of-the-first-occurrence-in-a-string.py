class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        i = 0 
        j = 0
        s = 0
        while i < len(haystack):
            if j == 0  and haystack[i]!=needle[0]:
                i+=1
            elif j == 0  and haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
                else:
                    i+=1
             
                
                    
        return -1
                        
                    
                    
        
        