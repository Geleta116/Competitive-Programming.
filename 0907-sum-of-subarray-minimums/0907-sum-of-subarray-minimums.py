class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        IDEA BEHIND THE CODE:- 
        We will create a monotonic increasing stack 
        and when we encounter a smaller value than the top of the stack we will pop the stack
        and count for how manu numbers the popped value was minimum for and we do this by multiplication
        
        pre will store the difference of the index of the first lower value
        post will store the difference between the index of the current and the popped value
        then we will multiply pre and post and then multiply it by the value of the popped value
        and then we will store it.
        
        """
        stack = []
        #we appended a zero to remove all elements if the stack isnt empty at the end
        arr.append(0)
        minsum = 0
        
        #We will iterate over the arr and fill the stack appropriately
        for index,num in enumerate(arr):
            #if the stack is empty just add the value and the index
            if not stack:
                stack.append([num,index])
            else:
                #if the end of the stack is smaller than the current value just append to the stack
                if stack[-1][0] <= num:
                    stack.append([num,index])
                else:
                    # if the current value is smaller than the stack head we will pop it and calculate the
                    #number of pre and post subarray minimums
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
        
