class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for j in path.split("/"):
            stack.append(j)
        l = []
        for i in stack:
                if i == "." or not i:
                    continue
                elif i =="..":
                    if l:
                        l.pop()
                else:
                    l.append(i)
        return ("/"+"/".join(l))

    
