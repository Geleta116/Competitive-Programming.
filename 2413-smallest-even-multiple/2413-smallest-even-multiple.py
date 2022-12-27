class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        maxi = 10000
        for number in range(n,maxi):
            if number % n ==0 and number %2 == 0:
                return number
        
        
        