class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.output = 0
        def backtrack(index, xor):
            if index == len(nums):
                self.output += xor
                return 
            backtrack(index +1, xor^nums[index])
            backtrack(index + 1, xor)
        backtrack(0,0)
        return self.output
            
            