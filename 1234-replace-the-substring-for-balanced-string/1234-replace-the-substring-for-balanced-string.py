class Solution:
    def balancedString(self, s: str) -> int:
        
        count = collections.Counter(s)
        
        maxLen = n = len(s)  
        
        left = 0
       
        right = 0
        
        def isValid():
            return n/4 >= max(count.values())
        
        while right < n:
            count[s[right]] -= 1
            while isValid() and left < len(s):
                maxLen = min(maxLen, right - left + 1 )
                count[s[left]] += 1
                left += 1 
            right += 1
            
        return maxLen
                
        