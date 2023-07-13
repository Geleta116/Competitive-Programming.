class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        arr = [[1],[1,1]]
        
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        
        for index in range(2,numRows):
            arr.append([1])
            
            for i in range(len(arr[-2])):
                if (i + 1) >= len(arr[-2]):
                    arr[-1].append(1)
                   
                
                else:
                    arr[-1].append(arr[-2][i] + arr[-2][i + 1])
        return arr