class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        k = -2
        sol = 0
        trip = len(piles)
        while trip>=3:
            sol+=int(piles[k])
            k-=2
            trip-=3
            
        return sol
        
