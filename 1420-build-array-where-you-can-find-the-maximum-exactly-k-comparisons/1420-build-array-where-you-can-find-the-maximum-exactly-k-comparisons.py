class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        
        @cache
        def backtrack(idx, maxi, remain):
            if idx == n:
                if remain == 0:
                    return 1
                else:
                    return 0
            
            
            output = (maxi * backtrack(idx + 1, maxi, remain)) % ( 10 ** 9 + 7)
            for i in range(maxi + 1, m + 1):
                output += backtrack(idx + 1, i, remain  - 1 ) % (10 ** 9 + 7)
            return output
        
        return backtrack(0,0,k) % ( 10 ** 9 + 7)