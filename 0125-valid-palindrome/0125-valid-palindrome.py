class Solution:
    def isPalindrome(self, s: str) -> bool:
            if s[0]==s[-1]==" ":
                return True
            else:
                t = ""
                s = s.upper()
                for l in range(len(s)):
                    if 65<=ord(s[l])<=90 or 97<=ord(s[l])<=122 or 48<=ord(s[l])<=57 :
                        t+=s[l]
                i = 0
                j = len(t)-1
                while i<j:
                    if t[i]!=t[j]:
                        return False
                    i+=1
                    j-=1
                return True
                    
        