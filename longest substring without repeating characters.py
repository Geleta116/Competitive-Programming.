class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        start = 0
        end= 0
        maxi = 0
        while end<len(s)-1:
            if s[end+1] not in s[start:end+1]:
                end +=1
                maxi = max(maxi,end-start+1)
            else:
                start +=1
                
        return(maxi)
                
