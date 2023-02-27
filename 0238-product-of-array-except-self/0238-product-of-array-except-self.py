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
        