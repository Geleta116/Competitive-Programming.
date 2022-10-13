class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp=sorted(score,reverse=False)
        ans = []
        for i in score:
            if temp.index(i)==len(temp)-1:
                ans.append("Gold Medal")
            elif temp.index(i)==len(temp)-2:
                       ans.append("Silver Medal")
            elif temp.index(i)==len(temp)-3:
                      ans.append("Bronze Medal")
            else:
                       ans.append(str(len(temp)-temp.index(i)))
                       
        return ans