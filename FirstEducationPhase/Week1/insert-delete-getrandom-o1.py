from random import randint
class RandomizedSet:

    def __init__(self):
        self.values={}
        self.indexes={}
        self.cur=0
    def insert(self, val: int) -> bool:
        if val not in self.values:
            self.values[val]=self.cur
            self.indexes[self.cur]=val
            self.cur+=1
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        if val in self.values:
            del self.indexes[self.values[val]]
            del self.values[val]
            return True
        else:
            return False
    def getRandom(self) -> int:
        while True:
            index=randint(0,self.cur)
            if index in self.indexes:
                return self.indexes[index]
        



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()