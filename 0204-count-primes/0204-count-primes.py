class Solution:
    def countPrimes(self, n: int) -> int:
        counter = [True for num in range(n)]
        if len(counter ) <= 2:
            return 0
        counter[0] = counter[1] = False
        start = 2
        count = 0
        while start * start <= n - 1:
            if counter[start]:
                extension = start * start
                while extension <= n - 1:
                    counter[extension] = False
                    extension += start
              
            start += 1
        
        count = 0
        for item in counter:
            if item:
                count += 1
        
        return count
        