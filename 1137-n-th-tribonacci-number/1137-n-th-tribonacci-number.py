class Solution:
    def tribonacci(self, n: int) -> int:
        first = 0
        second = 1
        third = 1
        if n  == 1 or n == 2:
            return 1
        elif n == 0:
            return 0
        
        for i in range(3,n + 1):
            temp = third
            third = first + second + third
            first = second
            second = temp
            
            
        return third
        
        
        
        
    


        