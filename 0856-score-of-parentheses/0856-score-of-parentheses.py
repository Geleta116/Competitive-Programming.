class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        current = 0
        for char in s:
            if char == "(":
                stack.append(current)
                current = 0
            else:
                current = stack.pop() + max(current*2,1)
        return current
        
       