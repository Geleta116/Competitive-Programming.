class Solution:
    def jump(self, nums: List[int]) -> int:
        dpdict = defaultdict(int)
        dpdict[len(nums) - 1] = 0
        def dp(idx):
            
            if idx == len(nums) - 1:
                return 0
            
            if idx in dpdict:
                return dpdict[idx]
            
            min_jump = float("inf")
            for i in range(idx + 1, min(len(nums), nums[idx] + idx + 1)):
                if i in dpdict:
                    store = dpdict[i]
                else:
                    store = dp(i)
                    dpdict[i] = store 
                if store != float("inf"):
                    min_jump = min(min_jump, store+1)
            dpdict[idx] = min_jump
            return min_jump
       
        return dp(0)



