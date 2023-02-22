class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        if len(s)==0:
            return 0
        
        length = 1
        counter = defaultdict(int)
        for right in range(len(s)):
            while s[right] in counter:
                counter.pop(s[start])
                start += 1
            counter[s[right]]+=1
            length = max(length,right-start+1)
        return length
            
                
              
             
              

                
        
            
            