class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for read in range(len(nums)):
            while read + 1 != nums[read]:
                current = nums[read]
                if nums[current - 1] == nums[read]:
                    break
                nums[read], nums[current - 1] = nums[current -1 ], nums[read]
                
        output = []
        for index,number in enumerate(nums):
            if index != number - 1:
                output.append(index + 1)
        return output
                