class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        out = []
        temp = []
        m = len(matrix[0])
        d = 0
        while d < m:
            i = 0
            while i<len(matrix):
                temp.append(matrix[i][d])
                i+=1
            out.append(temp)
            temp = []
            d+=1
        return out


    
