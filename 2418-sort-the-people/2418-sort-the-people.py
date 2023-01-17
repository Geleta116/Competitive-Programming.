class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # return names.sort(key = lambda x : x in heights, reverse = True)
        
        for j in range(len(names)-1):
            for k in range(j,len(names)):
                if heights[k]>heights[j]:
                    names[k], names[j] = names[j], names[k]
                    heights[k], heights[j] = heights[j], heights[k]
        
        return names
                
            
