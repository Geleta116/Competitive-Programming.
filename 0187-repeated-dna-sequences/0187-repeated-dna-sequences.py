class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10:
            return ""
        elif len(s) == 10:
            return ""
        else:
            i = 0
            j = 9
            dic = {}
            while j<len(s):
                dic[s[i:j+1]] = 1 + dic.get(s[i:j+1],0)
                i+=1
                j+=1
            out = []
            for a in dic:
                if dic[a]>1:
                    out.append(a)
            return out
                    
            
        