class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxi = arr[0]
        if len(arr)<3:
            return False
        else:
            inc = True
            dec = True
            indi = 0
            for i in range(1,len(arr)):
                if arr[i]==arr[i-1]:
                    return False
                elif arr[i] < arr[i-1]:
                    indi = i-1
                    break
            if indi == 0:
                return False
            for j in range(indi+1, len(arr)):
                if arr[j] >= arr[j-1]:
                    return False
            return True
                