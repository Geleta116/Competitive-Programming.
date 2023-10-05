class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dpdict = defaultdict(int)
        def dp(idx):
            # print(idx)
            if idx == len(nums) - 1:
                return True
            if idx in dpdict:
                return dpdict[idx]
            
            for i in range(idx + 1, min(len(nums), nums[idx] + idx+1)):
                if i in dpdict:
                    store = dpdict[i]
                else:
                    store = dp(i)
                    dpdict[i] = store
                if store:
                    return True
            dpdict[idx] = False
            return False
            
        return dp(0)
    
    
    