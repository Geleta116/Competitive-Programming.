class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = []
        for permutation in nums:
            answer.append(nums[permutation])
        return answer
        