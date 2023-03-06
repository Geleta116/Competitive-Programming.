class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        arr.append(0)
        minsum = 0
        for index,num in enumerate(arr):
            
            if not stack:
                stack.append([num,index])
            else:
                if stack[-1][0] <= num:
                    stack.append([num,index])
                else:
                    while stack and stack[-1][0] > num:
                        value,ind = stack.pop()
                        pre = index - ind
                        if stack:
                            post = ind - stack[-1][1]
                        else:
                            post = ind + 1
                        minsum += pre * post * value
                    stack.append([num,index])
            
             
        return minsum % (10**9 + 7)
                    
                    
                
                
        
        
        
        
        
        #don't forget to return in modulo 10**9 + 7
        