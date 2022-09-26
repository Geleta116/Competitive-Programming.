class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(len(nums)):
            pre.append(pre[i]*nums[i])
        pre = pre[1:]
        post = [1]
        l = 0
        m = len(nums)-1
        while l<m:
            nums[l],nums[m]=nums[m],nums[l]
            l+=1
            m-=1    
        for j in range(len(nums)):
            post.append(post[j]*nums[j])
        post = post[1:]
         
        k = 0
        c = len(post)-1
        while k<c:
            post[k],post[c]=post[c],post[k]
            k+=1
            c-=1 
        out = []
        for a in range(len(pre)):
            if a == 0:
                out.append(1*post[a+1])
            elif a ==  len(pre)-1:
                out.append(pre[a-1]*1)
            else:
                out.append(pre[a-1]*post[a+1])
        return out
    
    '''
    I have also tried the below solution and it got accepted
    class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        out = [1]
        for i in range(len(nums)-1):
            out.append(pre*nums[i])
            pre = out[i+1]
        
        for j in range(len(out)-1,-1,-1):
            out[j] = post * out[j]
            post = post*nums[j]
        return out
            
        
            
    '''
