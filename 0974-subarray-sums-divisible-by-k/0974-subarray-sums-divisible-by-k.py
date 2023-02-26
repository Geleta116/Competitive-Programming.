class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        count = [1] + [0] * k
        for a in nums:
            prefix = (prefix + a) % k
            res += count[prefix]
            count[prefix] += 1
        return res