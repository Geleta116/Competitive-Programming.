class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = ""
        num = 0
        for index in range(len(s)):
            if s[index] == "[":
                stack.append(current)
                stack.append(num)
                current = ""
                num = 0
            elif s[index] == "]":
                curnum = stack.pop()
                considered = stack.pop()
                current = considered + current * curnum
            elif s[index].isdigit():
                num = num*10 + int(s[index])
            else:
                current += s[index]
                
        return current
                
                