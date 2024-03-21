class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        running_product = 1
        output_count = 0
        for right in range(len(nums)):
            running_product *= nums[right]
            while running_product >= k and left <= right:
                running_product //= nums[left]
                left += 1
           
            output_count += (right - left + 1)
        return output_count
             
