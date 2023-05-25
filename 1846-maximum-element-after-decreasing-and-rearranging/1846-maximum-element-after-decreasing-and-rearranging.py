class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        arr[0] = 1
        for item in range(1, len(arr)):
            if arr[item] - arr[item - 1] == 1 or arr[item] == arr[item - 1]:
                continue
            else:
                arr[item] = arr[item - 1] + 1
        return arr[-1]
        
        