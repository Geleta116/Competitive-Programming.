class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return [] 
        l1 = []
        for i in s:
            l1.append(i)
        l2 = []
        for j in p:
            l2.append(j)
        ct2 = dict(Counter(l2))
        
        start = 0
        out = []
        ct1 = {}
        for x in range(len(l1)):
            ct1[l1[x]] = 1 + ct1.get(l1[x],0)
            if (x-start+1)==len(l2):
                if ct1 == ct2:
                    out.append(start)
                ct1[l1[start]]-=1
                if ct1[l1[start]]<1:
                    del ct1[l1[start]]
                start+=1
        return out
    
            
            
        