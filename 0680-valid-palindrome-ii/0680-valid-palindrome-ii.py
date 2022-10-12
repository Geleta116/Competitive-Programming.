class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                t = s[:i]+s[i+1:]
                t2 = s[:j]+s[j+1:]
                return t == t[::-1] or t2 == t2[::-1]
            i+=1
            j-=1
        return True