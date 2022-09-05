from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
            answer = 0
            count = dict(Counter(nums))
            for i in count:
                if ((k-i)in count) and (count[k-i]>0):
                    answer+=min(count[i],count[k-i])

            return(answer//2)

    
    
