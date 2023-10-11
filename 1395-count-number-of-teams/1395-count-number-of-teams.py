class Solution:
    def numTeams(self, rating: List[int]) -> int:
        @cache
        def dp( currIdx, n):
            
            if n == 3:
                return 1
            
            count = 0
            for idx in range(currIdx, len(rating)):
                if rating[idx] > rating[currIdx]:
                    count += dp( idx, n + 1)
            return count
        @cache
        def secdp(  currIdx, n):
            
            if n == 3:
                return 1
            
            count = 0
            for idx in range(currIdx, len(rating)):
                if rating[idx] < rating[currIdx]:
                    count += secdp( idx, n + 1)
            return count
        
        output = 0
        for ids in range(len(rating)):
            output += dp( ids, 1)
            output += secdp(ids, 1)
            
        return output
                    