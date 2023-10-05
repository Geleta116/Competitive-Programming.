class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        @cache
        def dp(idx):
            # print(idx)
            if idx == len(nums) - 1:
                return True
            for i in range(idx + 1, min(len(nums), nums[idx] + idx+1)):
                # print(idx,i)
                store = dp(i)
                if store:
                    return True
            return False
            
        return dp(0)