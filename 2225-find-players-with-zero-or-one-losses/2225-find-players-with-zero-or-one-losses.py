class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = []
        loses =[]
        for i in matches:
            wins.append(i[0])
        wins = list(set(wins))
        
        for j in matches:
            loses.append(j[1])
            
        lose = dict(Counter(loses))
        print(lose)
        
        out = []
        win = []
        lost = []
        for a in wins:
            if a not in lose :
                win.append(a)
        win.sort()
        out.append(win)
        
        for j in lose:
            if lose[j] == 1:
                lost.append(j)
        lost.sort()
        out.append(lost)
        
        return out