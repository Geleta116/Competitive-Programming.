class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        new_stack = []
        op = ["+","-","*","/"]
        for token in tokens:
            if token not in op:
                new_stack.append(token)
            else:
                if token == "+":
                    token1 = int(new_stack.pop())
                    token2 = int(new_stack.pop())
                    new_stack.append(token1 + token2)
                elif token == "-":
                    token1 = int(new_stack.pop())
                    token2 = int(new_stack.pop())
                    new_stack.append(token2 - token1)
                elif token == "*":
                    token1 = int(new_stack.pop())
                    token2 = int(new_stack.pop())
                    new_stack.append(token1 * token2)
                elif token == "/":
                    token1 = int(new_stack.pop())
                    token2 = int(new_stack.pop())
                    new_stack.append(int(token2 / token1))
        return int(new_stack[0])
                