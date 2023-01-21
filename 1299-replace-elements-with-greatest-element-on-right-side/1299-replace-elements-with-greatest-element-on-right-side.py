class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        i = len(arr)-1
        while i>=0:
            store = arr[i]
            arr[i] = greatest
            if store > greatest:
                greatest = store
            i-=1
        return arr
        