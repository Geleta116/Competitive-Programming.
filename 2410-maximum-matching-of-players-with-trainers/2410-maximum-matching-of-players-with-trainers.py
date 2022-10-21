class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        print(players)
        print(trainers)
        out = 0
        j = 0
        for i in range(len(players)):
            
            for k in range(j,len(trainers)):
                if players[i]<=trainers[k]:
                    out += 1
                    j = k+1
                    break
            #print(out)
            print(j)
        return out
        