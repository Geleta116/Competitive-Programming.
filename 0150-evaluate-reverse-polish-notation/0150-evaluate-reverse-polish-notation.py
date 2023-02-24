class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        new_stack = []
        op = ["+","-","*","/"]
        for i in range(len(tokens)):
            if tokens[i] not in op:
                new_stack.append(tokens[i])
            else:
                if tokens[i] == "+":
                    token1 = int(new_stack.pop())
                    token2 = int(new_stack.pop())
                    new_stack.append(token1 + token2)
                elif tokens[i] == "-":
                    token1 = int(new_stack.pop())
                    token2 = int(new_stack.pop())
                    new_stack.append(token2 - token1)
                elif tokens[i] == "*":
                    token1 = int(new_stack.pop())
                    token2 = int(new_stack.pop())
                    new_stack.append(token1 * token2)
                elif tokens[i] == "/":
                    token1 = int(new_stack.pop())
                    token2 = int(new_stack.pop())
                    new_stack.append(int(token2 / token1))
        return int(new_stack[0])
                