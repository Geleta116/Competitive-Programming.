class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        result = []
        for each_num in nums:
            if each_num > 0:
                positive.append(each_num)
            else:
                negative.append(each_num)
        for item in range(len(positive)):
            result.append(positive[item])
            result.append(negative[item])
        return result
            
            