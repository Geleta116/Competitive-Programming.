class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        ret = [0]*len(nums)
        l = 0 
        m = 0
        for j in range(len(ret)):
            if j%2==0:
                ret[j] = even[l]
                l+=1
            else:
                ret[j] = odd[m]
                m+=1
        return ret
            
        