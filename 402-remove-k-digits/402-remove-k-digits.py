class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st1 = []
        i = 0
        while i<len(num):
                while k>0 and st1 and st1[-1]>num[i]:
                        st1.pop()
                        k-=1

                st1.append(num[i])
                i+=1
        st1 = st1[:len(st1)-k]
        res = ""
        for l in st1:
            res+=l
            
        if len(res)>0:
            return str(int(res))
        else:
            return "0"
                 