class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        out = 0
        
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                prev= i
                forw = i
                count = 1
                while prev> 0 and arr[prev]>arr[prev-1]:
                    count+=1
                    prev -= 1
                while forw < len(arr)-1 and arr[forw]>arr[forw+1]:
                    count+=1
                    forw +=1
                out = max(out, count)
        return out
    