class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        i = 0
        j = 1
        store = arr[j] -arr[i]
        while j < len(arr):
            curr = arr[j] - arr[i]
            if curr != store:
                return False
            j += 1
            i += 1
        return True
            