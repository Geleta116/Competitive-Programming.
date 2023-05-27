class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [-1 for _ in range(n + 1)]
        
        def fib(n):
            if n == 0:
                return 1
            
            if n < 0:
                return 0
            
            
            if  arr[n - 1] != -1:
                    return arr[n - 1]
            

            arr[n - 1] = fib(n -1) + fib(n - 2)
             
            return arr[n - 1]
        
        return fib(n)
            

       