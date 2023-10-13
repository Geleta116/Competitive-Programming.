class Solution:
    def factorial(self, n):
    
        if n <= 1:
            return 1
        return n * self.factorial(n - 1)
    
    def exponentiation(self, base, power):
        if power == 0:
            return 1
        if power % 2 == 0:
            store = self.exponentiation(base, power // 2)
            return store * store
        else:
            store = self.exponentiation(base, (power - 1 )// 2)
            return store * store * base
        
    def countOrders(self, n: int) -> int:
        return ((self.factorial(2 * n)) // self.exponentiation(2, n)) % (10**9 + 7)