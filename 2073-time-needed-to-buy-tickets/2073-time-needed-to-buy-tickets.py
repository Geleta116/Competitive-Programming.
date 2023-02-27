class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        out = 0
        while tickets[k] > 0:
            for item in range(len(tickets)):
                if tickets[item] > 0 and tickets[k]>0:
                    out += 1
                    tickets[item] -= 1
        return out
            
        
        