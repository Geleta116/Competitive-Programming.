class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        leng = len(s)
        if leng == 0:
            return 0
        out = 1
        d = defaultdict(int)
        
       
        while end < leng:
            d[s[end]]+=1
            while start < end  and d[s[end]] > 1:
                print(start, end)
                
                d[s[start]]-=1
                start += 1
                
            out = max(out,end-start+1)
            end += 1
            
             
        return out
              
             
              
            
           
        
                
        
            
            