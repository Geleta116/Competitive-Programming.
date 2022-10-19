class Solution:
    def removeDuplicates(self, s: str) -> str:
        s1 = []
        for i in s:
            if len(s1)==0:
                s1.append(i)
            else:
                if s1[-1]==i:
                    s1.pop()
                else:
                    s1.append(i)
        return "".join(s1)
    
        