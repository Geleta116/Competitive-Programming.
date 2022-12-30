class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        store = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                store[i+j+1].append(mat[i][j])
        store = dict(store)
        out = []
        for i in store :
            if i %2 != 0 :
                j = len(store[i])-1
                while j > -1:
                    out.append(store[i][j])
                    j-=1
            else:
                j = 0
                while j<len(store[i]):
                    out.append(store[i][j])
                    j+=1
        return out
                
        