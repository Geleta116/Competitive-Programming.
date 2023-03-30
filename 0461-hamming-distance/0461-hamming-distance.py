class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_length  = 0
        temp = x
        while temp:
            temp //= 2
            x_length += 1
        y_length  = 0
        temp = y
        while temp:
            temp //= 2
            y_length += 1
        
        if x_length >= y_length:
            difference = 0
            while x:
                temp1 = x & 1
                temp2 = y & 1
                if temp1 != temp2:
                    difference += 1
                y >>= 1
                x >>= 1
        else:
            difference = 0
            while y:
                temp1 = x & 1
                temp2 = y & 1
                if temp1 != temp2:
                    difference += 1
                y >>= 1
                x >>= 1
        return difference
            
                
        