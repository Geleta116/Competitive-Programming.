class Solution:
    def longestPrefix(self, s: str) -> str:
        lsp = [0 for _ in range(len(s))]
        i = 0
        j = 1
        
        while j < len(s):
            if s[j] == s[i]:
                i += 1
                lsp[j] = i
                j += 1
            
            else:
                if i  != 0:
                    i = lsp[i - 1]
                else:
                    lsp[j] = 0
                    j += 1
        if lsp[-1] == 0:
            return ""
       
        return s[len(s) - lsp[-1] :]
    