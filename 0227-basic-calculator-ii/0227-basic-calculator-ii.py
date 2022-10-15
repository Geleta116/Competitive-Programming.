class Solution:
    def calculate(self, ss: str) -> int:
        c_num = 0
        op = "+"
        s = ""
        for a in range(len(ss)):
            if ss[a]==" ":
                continue
            else:
                s+=ss[a]
        
        s+='+'
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                c_num = (c_num*10)+int(char)
            else:
                c_num = int(c_num)
                if op == '+':
                    stack.append(c_num)
                elif op == '-':
                    stack.append(-c_num)
                elif op == '*':
                    stack.append(stack.pop()*c_num)
                elif op =="/":
                    stack.append(int(stack.pop()/c_num))
                c_num = 0
                op = s[i]
        return sum(stack)
        

                
                    
        