class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        return self.build(s) == self.build(t)
    
    def build(self, s):
        stack = []
        for i in s:
            if i != "#":
                stack.append(i)
            elif stack:
                stack.pop()
        return stack