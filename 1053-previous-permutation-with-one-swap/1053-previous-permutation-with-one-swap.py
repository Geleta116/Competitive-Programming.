class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for start in range(n-2,-1,-1):
            if arr[start] > arr[start+1]:
                for end in range(n-1,start,-1):
                    if arr[end] < arr[start] and (end == start-1 or arr[end] != arr[end-1]):
                        arr[start],arr[end] = arr[end],arr[start]
                        return arr
        return arr
        