class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        index_1 = 0
        index_2 = 1
        index_3 = 2
        out = 0
        while index_3 < len(nums):
            if nums[index_1]< nums[index_2] + nums[index_3]:
                out = nums[index_1]+ nums[index_2] + nums[index_3]
                break
            index_1 += 1
            index_2 += 1
            index_3 += 1
        return out
       
        