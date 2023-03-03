class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = bisect_left(nums,target)
        last = bisect_right(nums,target)
        print(first,last)
        if first == len(nums)  or len(nums) == 0 or nums[first] != target or (((last - 1) > -1) and nums[last - 1] != target):
            return [-1, -1]
        else:
            return[first,last - 1]
        