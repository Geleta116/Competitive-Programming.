class Solution:
    def jump(self, nums: List[int]) -> int:
        dpdict = defaultdict(int)
        dpdict[len(nums) - 1] = 0
        
        def dp(idx):
            if idx == len(nums) - 1:
                return 0
            
            if idx in dpdict:
                return dpdict[idx]
            
            min_jumps = float('inf')  # Initialize min_jumps to positive infinity
            
            for i in range(idx + 1, min(len(nums), nums[idx] + idx + 1)):
                if i in dpdict:
                    jumps_to_end = dpdict[i]
                else:
                    jumps_to_end = dp(i)
                    dpdict[i] = jumps_to_end
                
                if jumps_to_end != float('inf'):
                    min_jumps = min(min_jumps, jumps_to_end + 1)
            
            dpdict[idx] = min_jumps
            return min_jumps
        
        return dp(0)
