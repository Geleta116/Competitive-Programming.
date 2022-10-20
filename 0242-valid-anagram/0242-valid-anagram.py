class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            st = set(s)
            ct = set(t)
            if ct != st:
                return False
            else:
                et = dict(Counter(s))
                dt = dict(Counter(t))
                for i in et:
                    if dt[i]!=et[i]:
                        return False
                return True
            
        
        