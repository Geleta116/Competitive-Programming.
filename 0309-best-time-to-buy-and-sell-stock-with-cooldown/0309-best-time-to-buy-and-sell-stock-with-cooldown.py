class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        def TreeTraverse(index, isBuying):
            if index >= len(prices):
                return 0
            if (index, isBuying) in dp:
                return dp[(index, isBuying)]
            
            if isBuying:
                buy = TreeTraverse(index + 1, not isBuying) - prices[index]
                coolDown = TreeTraverse(index + 1, isBuying)
                
                dp[(index, isBuying)] = max(buy, coolDown)
            else:
                sell = TreeTraverse(index + 2, not isBuying) + prices[index]
                coolDown = TreeTraverse(index + 1, isBuying)
                dp[(index, isBuying)] = max(sell, coolDown)
            return dp[(index, isBuying)] 
        
        return TreeTraverse(0,True)
                