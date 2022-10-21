class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        print(players)
        print(trainers)
        out = 0
        j = 0
        i = 0
        while i<len(players) and j<len(trainers):
                if players[i]<=trainers[j]:
                    out += 1
                    j +=1
                    i+=1
                else:
                    j+=1
            
        return out
        