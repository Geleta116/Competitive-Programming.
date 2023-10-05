class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxi, mini = nums.index(max(nums)), nums.index(min(nums))
        minimum = min(mini,maxi)
        maximum = max(mini,maxi)
        # print(minimum, maximum)
        return min(maximum + 1, len(nums) - minimum, len(nums) - maximum + minimum + 1)