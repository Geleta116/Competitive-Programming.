class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [ i for i in range(1,n+1)]
        indi = 0
        while len(arr)>1:
            indi = (indi + k -1)%len(arr)
            arr.pop(indi)
            indi = (indi)%len(arr)
            
        return arr[0]

        
        