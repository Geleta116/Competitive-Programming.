class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = []
        for l in nums:
            n.append(str(l))
        
        for i in range(len(n)):
            for j in range(i,len(n)):
                    a = ""
                    b = ""
                    a = n[i]+n[j]
                    b = n[j]+n[i]
                    if a>b:
                        continue
                    elif b>a:
                        n[j],n[i] = n[i],n[j]
        x = ""
        for m in n:
            x+=m
        if int(x) == 0:
            return (str(0))
        else:
            return(x)

        
        
