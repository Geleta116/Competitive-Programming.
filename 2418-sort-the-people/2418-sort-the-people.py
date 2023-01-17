class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # return names.sort(key = lambda x : x in heights, reverse = True)
        
        #         for name in range(len(names)-1):
        #             for height in range(name,len(names)):
        #                 if heights[height]>heights[name]:
        #                     names[k], names[j] = names[j], names[k]
        #                     heights[k], heights[j] = heights[j], heights[k]

        #         return names

        for i in range(len(heights)-1,-1,-1):
            mini = i
            for j in range(i,-1,-1):
                if heights[j]<heights[mini]:
                    mini = j
            heights[mini],heights[i] =  heights[i], heights[mini]
            names[mini], names[i] = names[i], names[mini]
            
        return names
          
        
                
            
