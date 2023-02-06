class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j = len(skill)-1
        carer = []
        summ = skill[0]+skill[-1]
        while i<j:
            
            if skill[i]+skill[j]!= summ:
                return -1
            else:
                carer.append([skill[i],skill[j]])
                i+=1
                j-=1
        out = 0
        for item in carer:
            s = item[0]*item[1]
            out+=s
        return out
            
        