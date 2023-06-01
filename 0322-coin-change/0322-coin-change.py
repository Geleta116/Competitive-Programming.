class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        output = float("inf")
        
        @cache
        def dp(summ):
            
            if summ == amount:
                return 0
            
            elif summ > amount:
                return float("inf")
            
            store = float("inf")
            
            for currcoin in coins:
                
                store = min(store, 1 + dp( summ + currcoin))
                
            return  store
        
        # for coin in coins:
            # current = dp( coin)
            
            # output = min(output, current)
        self.ans = dp(0)
        if self.ans  == float("inf"):
            return -1
        return self.ans
        
        
        