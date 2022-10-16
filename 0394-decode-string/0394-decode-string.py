class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        ss = []
        out = ""
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            elif i == "[" :
                ss.append((out,num))
                num = 0
                out = ""
            elif 97<=ord(i)<=122:
                out+=i
                
            elif i =="]":
                prev_s,prev_n = ss.pop()
                out = prev_s + prev_n*out
        return out
                
                
            