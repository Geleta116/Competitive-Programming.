class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        out = 0
        i = 0
        j = len(tokens)-1
        while i<=j:
            if power>=tokens[i]:
                power = power - tokens[i]
                i+=1
                score +=1
                out = max(out,score)
            elif power<tokens[i] and score>0:
                power = power + tokens[j]
                j-=1
                score -=1
            else:
                break
        return out