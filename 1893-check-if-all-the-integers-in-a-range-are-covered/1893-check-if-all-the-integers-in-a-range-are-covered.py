class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        c = 0
        for l in range(left,right+1):
            for i in ranges:
                if i[0]<=l<=i[1]:
                    c+=1
                    break

        return c == right-left + 1
                
       