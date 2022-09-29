class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n= len(arr)
        ct = Counter(arr)
        summ = 0
        out = 0
        c = ct.values()
        c = list(c)
        c.sort()
        i = -1
        while summ<n//2:
            summ += c[i]
            i -=1
            out+=1
            
        
        
        return out
