class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for numbers in range(n + 1):
            count = 0
            
            while numbers:
                temp = numbers
                numbers = numbers & 1
                if numbers != 0 :
                    count += 1
                numbers = temp >> 1
                
            output.append(count)
        return output
                
        