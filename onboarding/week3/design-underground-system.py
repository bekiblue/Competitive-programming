from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.check_in={}
        self.total=defaultdict(lambda :[0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.total[(self.check_in[id][0],stationName)][0]+=(t-self.check_in[id][1])
        self.total[(self.check_in[id][0],stationName)][1]+=1
        del self.check_in[id]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
            return  self.total[(startStation,endStation)][0]/self.total[(startStation,endStation)][1]
            


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# print(obj.checkIn(32,"Paradise",8)

