class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        store = []
        for item in mat:
            for j in item:
                store.append(j)
        compare = []
        rows = 0
        while rows < len(store):
            temp = []
            for cols in range(c):
                if (rows+cols) < len(store):
                    temp.append(store[rows+cols])
            compare.append(temp)
            rows += c
            
        if len(compare[-1]) == c and len(compare) == r:
            return compare
        return mat
            