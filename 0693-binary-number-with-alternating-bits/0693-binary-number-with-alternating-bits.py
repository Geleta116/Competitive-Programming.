class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        while n:
            first = n >> 1
            if n & 1  ==  first & 1:
                return False
            n >>= 1
        return True
        