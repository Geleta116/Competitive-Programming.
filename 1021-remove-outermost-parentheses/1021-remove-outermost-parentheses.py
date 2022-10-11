class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ss=[]
        out = []
        c = 0
        for i in s:
            ss.append(i)
            if i == '(':
                c+=1
            elif i==')':
                c-=1
            if c == 0:
                out+=ss[1:-1]
                ss = []
                
        return  "".join(out)
        