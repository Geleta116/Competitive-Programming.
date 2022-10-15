class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        out = []
        x = "Push"
        y = "Pop"
        #target = [1,3], n = [1,2,3]
        i = 0
        while i < n:
            if i+1 in target:
                out.append(x)
                
            else:
                if i == target[-1]:
                    break
                out.append(x)
                out.append(y)
            i+=1
        return out
        
            
        