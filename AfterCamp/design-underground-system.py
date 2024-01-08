class UndergroundSystem:

    def __init__(self):
        self.checkinStore = defaultdict(list)
        self.records = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkinStore[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.checkinStore[id][0], stationName) not in self.records:
            self.records[(self.checkinStore[id][0], stationName)] = [0,0]
        curr = self.records[(self.checkinStore[id][0], stationName)]
        self.records[(self.checkinStore[id][0], stationName)] = [curr[0] + (t - self.checkinStore[id][1]), curr[1] + 1 ]
        self.checkinStore.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        value = self.records[(startStation, endStation)]
        return value[0] / value[1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)