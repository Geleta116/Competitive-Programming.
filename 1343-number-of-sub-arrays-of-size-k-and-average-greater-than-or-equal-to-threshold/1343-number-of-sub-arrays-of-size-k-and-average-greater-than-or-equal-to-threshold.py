class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        temp = k
        out = 0
        summ = 0
        start = 0
        end = 0
        while temp>0 and end<len(arr):
            summ += arr[end]
            end+=1
            temp-=1
        end -=1
        while end<len(arr):
            av = summ/k
            if av>= t:
                out+=1
            if end<len(arr)-1:
                end+=1
                summ += arr[end]
                summ -= arr[start]
                start+=1
            else:
                break
        return out
            
        