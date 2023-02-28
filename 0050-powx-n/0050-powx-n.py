class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1 
        elif n == 1:
            return x
        elif n > 0 :
            if n%5 == 0:
                n = n//5
                temp = self.myPow(x,n)
                return temp*temp*temp*temp*temp
            else:
        
                n -= 1
                return x*self.myPow(x,n)
        else:
            n = -n
            n -= 1
            return 1/x*self.myPow(1/x,n)
        