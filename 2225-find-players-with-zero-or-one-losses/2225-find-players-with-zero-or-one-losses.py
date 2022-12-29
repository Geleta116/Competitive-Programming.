class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = []
        loses =[]
        for items in matches:
            wins.append(items[0])
        wins = list(set(wins))
        
        for items in matches:
            loses.append(items[1])
            
        lose = dict(Counter(loses))
        
        
        output = []
        win = []
        lost = []
        for winners in wins:
            if winners not in lose :
                win.append(winners)
        win.sort()
        output.append(win)
        
        for losers in lose:
            if lose[losers] == 1:
                lost.append(losers)
        lost.sort()
        output.append(lost)
        
        return output