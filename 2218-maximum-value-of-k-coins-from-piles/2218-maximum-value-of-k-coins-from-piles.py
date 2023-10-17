from functools import cache

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        prefixSum = []
        
        for idx in range(len(piles)):
            temp = [0]
            for coinIdx in range(len(piles[idx])):
                temp.append(temp[-1] + piles[idx][coinIdx])
            prefixSum.append(temp[:])
        
        
        def dp(index, leftMoves, prefixSum , memo ):
            if leftMoves == 0 or index == len(piles):
                return 0
            
            if ( index, leftMoves) in memo:
                return memo[(index,leftMoves)]
            
            currAns= 0
            for idx in range(min(leftMoves + 1, len(prefixSum[index]))):
                currAns = max(currAns, prefixSum[index][idx] + dp(index + 1, leftMoves - idx, prefixSum, memo))
            currAns = max(currAns, dp(index + 1, leftMoves, prefixSum, memo) )
            
            memo[(index, leftMoves)] = currAns
            return memo[(index, leftMoves)]
        
        memo = {}
        store = dp(0,k,prefixSum, memo)
        
        return store
            
            
            
                            
            