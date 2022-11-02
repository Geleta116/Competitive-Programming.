class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        if len(l)==1:
            return s
        else:
            i = 0
            j = len(l)-1
            while i<j:
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
            return " ".join(l)
            