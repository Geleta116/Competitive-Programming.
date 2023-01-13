class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dic = {"D":0,"U":0, "L":0,"R":0}
        for char in moves:
            dic[char]+=1
        if (dic["D"] - dic["U"] == 0)  and (dic["L"] - dic["R"]== 0) :
            return True
        else:
            return False
#         stack = []
#         for i in range(len(moves)):
#             if not(stack):
#                 stack.append(moves[i])
#             else:
#                 if moves[i] == "U":
#                     if stack[-1] == "D":
#                         stack.pop()
#                     else:
#                         stack.append("U")
#                 elif moves[i] == "D":
#                     if stack[-1] == "U":
#                         stack.pop()
#                     else:
#                         stack.append("D")
#                     #
#                 elif moves[i] == "R":
#                     if stack[-1] == "L":
#                         stack.pop()
#                     else:
#                         stack.append("R")
#                     #
#                 elif moves[i] == "L":
#                     if stack[-1] == "R":
#                         stack.pop()
#                     else:
#                         stack.append("L")
#                     #
                
            
          
        
#         if len(stack) == 0:
#             return True
#         else:
#             return False
          
                
                
            
        