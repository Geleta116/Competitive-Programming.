class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dp = {}
        output = 1
        
        
        for word in  sorted(words, key=len):
            dp[word] = 1
            
            for index in range(len(word)):
                checked = word[:index] + word[(index + 1) :]
                if checked in dp:
                    
                    dp[word] = max(dp[word] , dp[checked] + 1)
                    output = max(output, dp[word])
                    
        return output
    
   
  