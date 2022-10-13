class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        c = []
        for i in blocks:
            if i == "W":
                c.append(1)
            else:
                c.append(0)
        print(c)
        i = 0
        j = k-1
        l = []
        while j<len(c):
            l.append(sum(c[i:j+1]))
            j+=1
            i+=1
        return min(l)
            