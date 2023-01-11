class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = -1
        while i<len(s)+j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        """
        Do not return anything, modify s in-place instead.
        """
        