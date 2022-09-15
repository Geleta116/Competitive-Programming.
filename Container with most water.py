class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = -1
        out = 0
        while i<(len(height)+j):
            if height[i]!=height[j]:
                area = min(height[i],height[j])*((len(height)+j)-i)
                out = max(out,area)
                
                if height[i]>height[j]:
                    j-=1
                elif height[i]<height[j]:
                    i+=1
            else:
                area = (height[i])*((len(height)+j)-i)
                out = max(out,area) 
               
                i+=1
        return out
