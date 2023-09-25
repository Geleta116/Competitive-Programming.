class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        toBeSorted = zip(ages, scores)
        sortedList = sorted(toBeSorted)
        scores = [member[1] for member in sortedList]

        dp = [score for score in scores]
        
        for currIndex in range(len(scores)):
            
            for checkIndex in range(currIndex):
                
                if scores[checkIndex] <= scores[currIndex]:
                    dp[currIndex] =  max(dp[currIndex], scores[currIndex] + dp[checkIndex])
        
        return max(dp)
