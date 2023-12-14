class FrequencyTracker:

    def __init__(self):
        self.num={}
        self.freq={}

    def add(self, number: int) -> None:
        if number in self.num:
            self.freq[self.num[number]]-=1
            if self.freq[self.num[number]]==0:
                del self.freq[self.num[number]]
        self.num[number]=self.num.get(number,0)+1
        self.freq[self.num[number]]=self.freq.get(self.num[number],0)+1
    def deleteOne(self, number: int) -> None:
        if number in self.num:
            self.freq[self.num[number]]-=1
            if self.freq[self.num[number]]==0:
                del self.freq[self.num[number]]
            self.num[number]=self.num[number]-1
            if self.num[number]==0:
                del self.num[number]
            else:
                self.freq[self.num[number]]=self.freq.get(self.num[number],0)+1
    def hasFrequency(self, frequency: int) -> bool:
        return True if frequency in self.freq else False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)