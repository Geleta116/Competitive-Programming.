class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def backtrack(left, right):
            if left == right:
                return 1
            
            if left > right:
                return 0
            
            if s[left] == s[right]:
                return 2 + backtrack(left + 1, right - 1)
            
            return max(backtrack(left + 1, right), backtrack(left, right - 1))
            
        return backtrack(0,len(s) - 1)