class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        summ = 0
        for i in cardPoints:
            summ+=i
        n = len(cardPoints)
        if n == k :
            return summ
        size_win = n-k-1
        win = 1
        out = 0
        start = 0
        sum_win = cardPoints[0]
        if n-k == 1:
                for a in cardPoints:
                    out = max(out,summ-a)
                return out
        
        else:
            
            while win < n:
                if win-start < size_win:
                    sum_win +=cardPoints[win]
                    win+=1
                elif win-start == size_win:
                    sum_win +=cardPoints[win]
                    break
                else:
                    break
            while win < n:
                    out = max(out,summ - sum_win)
                    sum_win -= cardPoints[start]
                    win+=1
                    start+=1
                    if win<n:
                        sum_win += cardPoints[win]
        
            
            
            return out
                
            
            
        
            
        
        