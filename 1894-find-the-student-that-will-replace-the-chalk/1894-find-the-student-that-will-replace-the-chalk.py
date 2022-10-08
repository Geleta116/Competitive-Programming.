class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot = 0
        for l in chalk:
            tot+=l
        k = k%tot
        if len(chalk)==1:
            return 0
        if k == 0:
            return 0
        summ = 0
        i = 0
        while summ<k:
            summ +=chalk[i]
            if summ>k:
                return i
            elif summ==k:
                return i+1
            else:
                i+=1
        
        
        