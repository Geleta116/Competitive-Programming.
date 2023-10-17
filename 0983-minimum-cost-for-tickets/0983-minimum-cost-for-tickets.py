class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travelDays = set(days)
        
        @cache
        def dp(day):
           
            if day <= 0:
                return 0
            
            if day in travelDays:
                minSofar = min(costs[0] + dp(day - 1), costs[1]  + dp(day - 7), costs[2] + dp(day - 30))
                return minSofar
            
            else:
                return dp(day - 1)
                
        return dp(days[-1])
                    
        

           