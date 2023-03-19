class TopVotedCandidate:
   

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leader = self.persons[0]
        self.values = defaultdict(int)
        self.values[self.leader] += 1
        for item in range(1,len(self.persons)):
            self.values[self.persons[item]] += 1
            if self.values[self.leader] > self.values[self.persons[item]]:
                self.persons[item] = self.leader
                
                
            else:
                self.leader =  self.persons[item]

    def q(self, t: int) -> int:
        def validate(mid,t):
            if self.times[mid] >= t:
                return True
            return False

        start = -1
        end = len(self.persons)
        while end > start + 1:
            mid = start + (end - start ) // 2
            if validate(mid,t):
                end = mid
            else:
                start = mid
        if end >= len(self.times):
            return self.persons[-1]
        else:
            if self.times[end] == t:
                return self.persons[end]
            else:
                if end == 0:
                    return self.persons[0]
                else:
                    return self.persons[end - 1]
      
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
