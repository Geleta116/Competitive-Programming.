class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) <3:
            return 0
        
        i = 0 
        j =1
        k = 2
        
        countA = 0
        countB = 0
        
        while k < len(colors):
            if colors[i] == "A" and colors[j] == "A" and colors[k] == "A":
                countA += 1
               
            elif  colors[i] == "B" and colors[j] == "B" and colors[k] == "B":
                countB += 1
                
            i += 1
            j += 1
            k += 1
            
        if countA > countB:
            return 1
        return 0
    
    