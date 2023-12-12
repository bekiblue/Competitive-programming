class OrderedStream:

    def __init__(self, n: int):
        self.stream=[""]*n
        self.cur=0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1]=value
        cur=self.cur
        if idKey-1 == self.cur:
            for index in range(self.cur+1,len(self.stream)):
                if not self.stream[index]:
                    self.cur=index
                    break
            else:
               return self.stream[self.cur:] 
        return self.stream[cur:self.cur]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)