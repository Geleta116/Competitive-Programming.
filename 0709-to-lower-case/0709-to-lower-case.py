class Solution:
    def toLowerCase(self, s: str) -> str:
        b = s.split()
        a = []
        for i in b:
            temp = []
            for j in i:
                if j.isupper():
                    temp.append(j.lower())
                else:
                    temp.append(j)
            a.append(temp)
        out = []
        for c in a:
            out.append("".join(c))
        

        return " ".join(out)
        