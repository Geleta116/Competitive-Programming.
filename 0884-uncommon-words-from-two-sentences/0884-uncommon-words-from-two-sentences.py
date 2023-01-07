class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        c = Counter(A.split() + B.split())
        res = []
        for i in c:
            if c[i] == 1:
                res.append(i)

        return res
