class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        elif n>0 and n%3==0:
            temp = self.myPow(x,n/3)
            return temp*temp*temp
        elif n>0:
            n= n-1
            return x* self.myPow(x,n)
        else:
            x = 1/x
            n = -n
            n=n-1
            return x*self.myPow(x,n)
