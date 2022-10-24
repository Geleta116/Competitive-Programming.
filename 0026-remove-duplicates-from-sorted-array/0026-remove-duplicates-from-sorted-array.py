class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = 1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                nums[temp] = nums[i+1]
                temp+=1
        return temp
        