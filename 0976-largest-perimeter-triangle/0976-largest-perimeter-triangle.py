class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        i = 0
        j = 1
        k = 2
        out = 0
        while k < len(nums):
            if nums[i]< nums[j] + nums[k]:
                out = nums[i]+ nums[j] + nums[k]
                break
            i += 1
            j += 1
            k += 1
        return out
       
        