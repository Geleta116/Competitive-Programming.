class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        store = len(arr)
        i = 0
        while i <len(arr):
            if i != len(arr)-1 and arr[i] == 0:
                arr.insert(i+1,0)
                i+=2
            elif i == len(arr)-1 and arr[i] == 0:
                arr.append(0)
                break
            else:
                i+=1
        while len(arr)>store:
            arr.pop()
            
        
        """
        Do not return anything, modify arr in-place instead.
        """
        