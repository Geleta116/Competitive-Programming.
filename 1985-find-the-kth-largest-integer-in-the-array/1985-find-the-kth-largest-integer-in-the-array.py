class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(map(int, nums))
        k = len(nums)-k
        return(str(nums[k]))
       
       