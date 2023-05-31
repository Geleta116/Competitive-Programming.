class Solution:
    def tribonacci(self, n: int) -> int:
        self.arr = []
        if n  == 1 or n == 2:
            return 1
        elif n == 0:
            return 0
        self.arr.append(0)
        
        for i in range(2):
            self.arr.append(1)
            
        
        for i in range(3,n + 1):
            self.arr.append(self.arr[i - 2] + self.arr[i - 1] + self.arr[i - 3])
        return self.arr[-1]
        
        
        
        
    


        