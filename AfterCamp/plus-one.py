class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(len(digits)):
            digits[idx] = str(digits[idx])
            
        large_int = int("".join(digits))
        large_int += 1
        large_int = str(large_int)
        output = []
        
        for i in large_int:
            output.append(int(i))
        return output
        