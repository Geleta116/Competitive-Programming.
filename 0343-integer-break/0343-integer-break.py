class Solution:
    def integerBreak(self, n: int) -> int:
        tmp = n%3
        if n == 3:
            return 2
        if n == 2:
            return 1
        if tmp == 1:
            return 3**(n//3-1)*4
        if tmp == 2:
            return 3**(n//3)*2
        if tmp == 0:
            return 3**(n//3)
        