class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        #count the numbers in deck
        count = Counter(deck)
        counts = [count[num] for num in count]
        
        
        # find the gcd of the counts and if it is 1 return False
        # if the gcd is not equals to one return True
        
        def gcd(a,b):
            
            while b:
                a,b = b, a % b
            
            return a
        if len(counts) < 2:
            if counts[0] == 1:
                return False
            return True
                
            
            
        gcds = gcd(counts[0], counts[1])
        
        for item in counts:
            gcds = gcd(gcds , item)
            
            if gcds == 1:
                return False
        
        return True
                
        
        
        
        
        
        
        