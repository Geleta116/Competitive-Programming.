class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        nums = set(nums)
        primes = set()
        def allPrimes(number):
            start = 2
            if number == 2 or number == 3:
                primes.add(number)
                return
            
            item = number
            while start  <= number:
                
                while item % start == 0:
                        item = item // start
                        primes.add(start)
                    
                start += 1
       
        for product in nums:
            
            allPrimes(product)
        
        
        return len(primes)
                
                    