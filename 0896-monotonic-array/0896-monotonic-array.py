class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        temp = sorted(nums)
        if temp ==  nums:
            return True
        else:
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]:
                    continue
                else:
                    return False
            return True


        