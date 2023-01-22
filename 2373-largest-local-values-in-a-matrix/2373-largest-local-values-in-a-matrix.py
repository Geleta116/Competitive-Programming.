class Solution:
    def largestLocal(self, matrix: List[List[int]]) -> List[List[int]]:
        out = []
        n = len(matrix)
        for i in range(n-2):
            temp = []
            for j in range(n-2):
                maxi = 0
                for r in range(i,3+i):
                    for c in range(j,3+j):
                        maxi = max(maxi, matrix[r][c])
                temp.append(maxi)
            out.append(temp)
        return out
                        
                