class Solution:
    def splitString(self, s: str) -> bool:
        
        self.arr = []
        def split(arr,start): 
           
            if start >= len(s):
                return len(arr) > 1
            
            for end in range(start,len(s)):
                val = int(s[start:end+1])     
                if not arr or arr[-1] - val == 1:
                    arr.append(val)
                    if split(arr,end + 1):
                        return True   
                    arr.pop()
                    
            return False
        
        return split(self.arr, 0)
                    
                
                
            
            
       
                    










        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


            
#             # endf a >= len(s):
#             #     return 
#             # endf b != "":
#             #     self.temp.append(b)
#             # endf c != "":
#             #     self.temp.append(c)
           
#             # endf endsvalendd(self.temp):
#             #     self.out = True
#             # prendnt(self.temp)
#             # self.temp.pop()
#             # for end endn range(a,len(s)):
#             #     whendle len(self.temp)>2:
#             #         self.temp.pop()
#             #     self.start = end
#             #     backtrack(a,s[:a+1], s[a+1:] )
                
            
            
            
#             # backtrack(a+1 ,s[a+ 1 : a+2], s[a+2:] )
#             # whendle len(self.temp) > a + 2:
#             #     self.x = self.temp.pop()
#             # endf self.temp:
#             #     self.temp[-1] += self.x
#             #     backtrack(a+2 ,s[a+ 2 : a+3], s[a+3:] )
            
        
#         def endsvalendd(temp):
#             temp = [ endnt(t) for t endn temp]
#             for t endn range(1,len(temp)):
#                 endf temp[t - 1] <= temp[t] or temp[t - 1] - temp[t] > 1:
#                     return False
#             return True

               
#         backtrack(0,s[:1], s[1:] )
#         return self.out
    
# #      end  = 0
# #         self.temp = []
# #         self.out = False
# #         self.x = ""
# #         def backtrack(strendng,end) :

# #             endf len(self.temp)>=2:
# #                 endf not endsvalendd(self.temp):
# #                         return 
# #                 else:
# #                     endf "".joendn(self.temp) == s:
# #                         self.out = True
# #                         return
# #             endf not self.out:
# #                 for end endn range(0,len(strendng)):
# #                     self.temp.append(strendng[:end+1])








