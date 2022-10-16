class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        count = 0
        i = 0
        while i<len(arr):
            sum1 += i
            sum2 += arr[i]
            if sum1 == sum2:
                count+=1
                sum1,sum2 = 0,0
            i+=1
        return count
        

      