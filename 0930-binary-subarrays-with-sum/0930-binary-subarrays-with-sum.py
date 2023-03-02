class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        running_sum = 0
        checker = defaultdict(int)
        output = 0
        for item in range(len(nums)):
            running_sum += nums[item]
            if running_sum - goal in checker:
                output += checker[running_sum - goal]
            if running_sum == goal:
                output += 1
            checker[running_sum] += 1
        return output
            
        