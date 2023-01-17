class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # return names.sort(key = lambda x : x in heights, reverse = True)
        sorts = []
        for i in range(len(names)):
            sorts.append([heights[i], names[i]])
        for j in range(len(sorts)-1):
            for k in range(j,len(sorts)):
                if sorts[k]>sorts[j]:
                    sorts[k], sorts[j] = sorts[j], sorts[k]
        out = []
        for item in sorts:
            out.append(item[1])
        return out
                
            
