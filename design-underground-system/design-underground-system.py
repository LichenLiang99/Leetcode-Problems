class UndergroundSystem:

    def __init__(self):
        self.ids = {}
        self.pairs = collections.Counter()
        self.freq = collections.Counter()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, t2 = self.ids[id]
        self.pairs[(start, stationName)] += t - t2
        self.freq[(start, stationName)] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.pairs[startStation, endStation] / self.freq[startStation, endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)