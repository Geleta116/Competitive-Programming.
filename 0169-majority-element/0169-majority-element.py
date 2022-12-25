class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1
            if m[n] > len(nums)//2:
                return n
        