class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
            n = []
            m = len(l)
            for i in range(m):
                queryy =  nums[l[i]:r[i]+1]
                queryy.sort()
                ist = True
                if len(queryy)<2:
                    n.append(False)

                elif len(queryy)==2:
                    n.append(True)

                else:
                    dif = queryy[1]-queryy[0]
                    for j in range(1,len(queryy)-1):
                        if queryy[j+1]-queryy[j]!= dif:
                                ist = False
                                
                    n.append(ist)
            return n


                
        
