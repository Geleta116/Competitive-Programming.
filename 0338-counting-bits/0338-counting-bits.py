class Solution:
    def countBits(self, n: int) -> List[int]:
        
        previous = defaultdict(int)
        for numbers in range(n + 1):
            count = 0
            first = numbers
            while numbers:
                temp = numbers
                numbers = numbers & 1
                if numbers != 0 :
                    count += 1
                numbers = temp >> 1
                if numbers in previous:
                    count += previous[numbers]
                    break
            previous[first] = count
            
        
        return previous.values()
                
        