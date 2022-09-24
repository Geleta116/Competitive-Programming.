class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pre_sum = [0]
        temp = []
        for l in nums:
            if l%2==0:
                temp.append(0)
            elif l%2!=0:
                temp.append(1)
                
        p = {0:1}
        out = 0
        summ = 0
        for i in temp:
            summ +=i
            diff = summ-k
            out+=p.get(diff,0)
            p[summ ]= 1+p.get(summ,0)
            
        return out
