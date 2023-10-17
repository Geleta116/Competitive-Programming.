class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7

        def fast_pow(base, exp):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result 

        n -= 1
        if n % 2 == 0:
            e  = (n // 2) + 1
            o =  (n // 2)
        else:
            e = ((n - 1) // 2) + 1
            o = e
      
        return (fast_pow(5, e) * fast_pow(4, o)) % mod
