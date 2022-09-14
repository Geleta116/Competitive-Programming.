class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        new_stack = []
        op = ["+","-","*","/"]
        for i in range(len(tokens)):
            if tokens[i] not in op:
                new_stack.append(tokens[i])
            elif tokens[i] in op:
                t1 = new_stack.pop()
                t2 = new_stack.pop()
                if tokens[i]!="-" and tokens[i]!="/":
                    val = str(t1) + str(tokens[i])+ str(t2)
                    inp = eval(val)
                    new_stack.append(inp)
                elif tokens[i]=="-" or tokens[i]=="/":
                    val = str(t2) + str(tokens[i])+ str(t1)
                    inp = eval(val)
                    new_stack.append(int(inp))
        return int(new_stack[0])
            
        
