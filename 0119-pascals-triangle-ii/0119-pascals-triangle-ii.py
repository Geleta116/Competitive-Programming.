class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        line = [1]
        # return line
        def helper(rowIndex,k,line):
            if k == rowIndex:
                return line
            line.append(line[k] * (rowIndex-k) // (k+1))
            return helper(rowIndex,k+1,line)
        return helper(rowIndex,0,line)
            