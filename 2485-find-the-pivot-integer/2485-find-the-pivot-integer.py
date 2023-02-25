class Solution:
    def pivotInteger(self, n: int) -> int:
        summ = 0
        for i in range(1,n+1):
            summ += i
        current = 0
       
        for j in range(1,n+1):
            current += j
            
            if current == summ - current + j:
                return j
            
        return -1
        