class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pre = [0]
        for i in range(len(nums)):
            pre.append(pre[i]+nums[i])
        pre = pre[1::]
        out = []
        for j in queries:
            out.append(bisect.bisect_right(pre,j))
        return out
            
                
                    
                    
            