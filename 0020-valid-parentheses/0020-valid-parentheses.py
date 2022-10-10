class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = "({["
        closing = ")}]"
        if len(s)==1:
             return(False)
        else:
                for i in range(len(s)):
                    if s[i] in opening:
                        stack.append(s[i])
                        
                    else:
                        if s[i] == "]"   :
                            if len(stack)!=0:
                                if stack[-1]=="[":
                                    stack.pop()
                                else:
                                    return False
                            else:
                                return False
                        elif s[i] == ")"   :
                            if len(stack)!=0:
                                if stack[-1]=="(":
                                    stack.pop()
                                else:
                                    return False
                            else:
                                return False
                            
                        elif s[i] == "}"   :
                            if len(stack)!=0:
                                if stack[-1]=="{":
                                    stack.pop()
                                else:
                                    return False
                            else:
                                return False
                            
                if len(stack)==0:
                    return True
                else:
                    return False
                        