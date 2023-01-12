class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(j) for j in digits]
        x = "".join(digits)
        x = int(x)+1
        x = str(x)
        out = [int(i) for i in x]
        return out
        # end = digits[-1]
        # start = digits[0]
        # if end == 9:
        #     if start == 9 :
        #         digits = [0 for item in range(len(digits))]
        #         digits.insert(0,1)
        #     else:
        #         digits = [0 for item in range(len(digits))]
        #         start += 1
        #         digits[0] = start
        # else:
        #     digits[-1]+= 1
        # return digits