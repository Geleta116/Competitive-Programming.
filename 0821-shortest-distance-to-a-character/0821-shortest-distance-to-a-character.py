class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        out = [ float("inf") for _ in range(len(s))]
        
        left = 0
        right  = 0
        
        while right < len(s):
            if s[right] == c:
                while left < right:
                    out[left] = min(out[left] , right - left)
                    left +=1
                out[right] = 0
                right += 1
                while right < len(s) and s[right] != c:
                    out[right] = right  - left
                    right += 1
            else:
                right += 1
        return out
                    