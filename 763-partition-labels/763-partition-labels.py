class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maxi = {j:i for (i,j) in enumerate(s)}
        ans = []
        end = maxi[s[0]]
        size = 0
        for l,k in enumerate(s):
            size+=1
            if maxi[k] > end:
                end = maxi[k]
            if l == end:
                ans.append(size)
                size = 0
        return ans
            
            
            
            
                    
        
                
                
            
            
                
               
               
                
                
                
                
                    
                   