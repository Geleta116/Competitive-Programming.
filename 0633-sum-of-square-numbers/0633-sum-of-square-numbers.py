class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(math.sqrt(c))
        while start <= end:
            if start**2 + end**2 > c:
                end -=1
            elif start**2 + end**2<c:
                start += 1
            else:
                return True
        return False

                
        