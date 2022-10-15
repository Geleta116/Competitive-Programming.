class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        out = []
        x = "Push"
        y = "Pop"
        #target = [1,3], n = [1,2,3]
        for i in range(1,n+1):
            if i in target:
                out.append(x)
            else:
                out.append(x)
                out.append(y)
            if i == target[-1]:
                break
        return out
            
        