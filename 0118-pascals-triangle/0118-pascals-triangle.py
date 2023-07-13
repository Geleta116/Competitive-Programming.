class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr =[]
        for index in range(numRows):
            arr.append([1])
            if len(arr) >=2:
                for i in range(len(arr[-2])):
                    if (i + 1) >= len(arr[-2]):
                        arr[-1].append(1)
                    else:
                        arr[-1].append(arr[-2][i] + arr[-2][i + 1])
        return arr