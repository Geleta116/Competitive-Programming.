class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        s = [i for i in s]
        checker = defaultdict(int)
        ch = set()
        for char in s:
            checker[char] += 1
        
        for char in s:
            
            if not stack:
                checker[char] -= 1
                stack.append(char)
                ch.add(char)
            else:
                if stack[-1]<char and char not in ch:
                    checker[char] -= 1
                    stack.append(char)
                    ch.add(char)
                elif stack[-1] == char:
                    checker[char] -= 1
                    
                else:
                    if char not in ch:
                        while stack and  stack[-1] > char and checker[stack[-1]] > 0:
                            ch.remove(stack[-1])
                            stack.pop()
                            
                        checker[char] -= 1
                        stack.append(char)
                        ch.add(char)
                    elif char in ch:
                        checker[char] -= 1
                        
        answer = "".join(stack)
        return answer
                    
                
