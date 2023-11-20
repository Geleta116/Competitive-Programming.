class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        out = [[1], [1,1]]
        
        for i in range(1, numRows - 1):
            temp = [1]
            for j in range(i):
                temp.append(out[-1][j] + out[-1][ j + 1])
            
            temp.append(1)
            
            out.append(temp[:])
        
        return out
    
    