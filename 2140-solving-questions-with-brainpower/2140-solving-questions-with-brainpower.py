class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        lists = [i for (i,l) in questions]
        leng = len(questions)
        maxxi = 0
        for j in range(leng-1,-1,-1):
            if j + questions[j][1]+1 > leng-1:
                maxxi = max(lists[j],maxxi)
            else:
                maxxi = max(lists[j]+lists[j + questions[j][1]+1],maxxi)
            lists[j] = maxxi
        return lists[0]
        