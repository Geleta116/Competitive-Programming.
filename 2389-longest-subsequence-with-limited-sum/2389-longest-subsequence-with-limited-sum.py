class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pre = [0]
        for i in range(len(nums)):
            pre.append(pre[i]+nums[i])
        pre = pre[1::]
        j = 0
        out = []
        while j<len(queries):
            l = 0
            c = 0
            while l<len(pre):
                if pre[l] < queries[j]:
                    l+=1
                    c+=1
                elif pre[l]>queries[j]:
                    break
                else:
                    c+=1
                    break
            out.append(c)
            c = 0
            j+=1
        return out
                
                    
                    
            