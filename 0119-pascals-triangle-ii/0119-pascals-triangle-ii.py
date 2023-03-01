class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1 for _ in range(rowIndex + 1)]
        
        previous = self.getRow(rowIndex - 1)
        output = [1 for _ in range(rowIndex+1)]
        for index in range(rowIndex-1):
            output[index + 1] = previous[index] + previous[index + 1]
            
        return output
            
            
            