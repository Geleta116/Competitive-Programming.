class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count =  0
        for index in range(n):
            left =  right =  index
            
            while left > -1 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            left = index
            right  =  index + 1
            
            while left > -1 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
                
        return count