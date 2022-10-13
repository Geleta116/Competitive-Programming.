class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s)==0:
            return t
        l = [s[a] for a in range(len(s))]
        l.sort()
        print(l)
        d =  [t[b] for b in range(len(t))]
        d.sort()
        print(d)
        i = 0
        while i<len(l):
            if l[i]!=d[i]:
                return d[i]
            i+=1
        return d[i]
        