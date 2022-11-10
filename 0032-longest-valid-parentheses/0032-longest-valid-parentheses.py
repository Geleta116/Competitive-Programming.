class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        (()
        s = [()]
        c +=1 
        store = [1]
        
        """
        if len(s)==0 or len(s)==1:
            return 0
        stack = [-1]
        brac = 0
        out = 0
        while brac <len(s):
            if s[brac] =="(":
                stack.append(brac)
            elif s[brac]== ")":
                stack.pop()
                if not stack:
                    stack.append(brac)
                else:
                    out = max(out,brac-stack[-1])
            brac+=1
        return out
                    
               