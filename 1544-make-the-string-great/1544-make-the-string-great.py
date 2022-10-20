class Solution:
    def makeGood(self, s: str) -> str:
        t = []
        for i in s:
            if not t:
                t.append(i)
            else:
                if t[-1].isupper():
                        if i.isupper():
                            t.append(i)
                        else:
                            if i.upper()==t[-1]:
                                t.pop()
                            else:
                                t.append(i)
                else:
                     if i.islower():
                            t.append(i)
                     else:
                            if i.lower()==t[-1]:
                                t.pop()
                            else:
                                t.append(i)
           
        return "".join(t)
                    
        