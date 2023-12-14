class Bitset:

    def __init__(self, size: int):
        self.bitsets=["0"]*size
        self.ones=0
        self.flipped=False
    def fix(self, idx: int) -> None:
        if not self.flipped and self.bitsets[idx] == "0" :
            self.bitsets[idx]="1"
            self.ones+=1
        elif self.flipped and self.bitsets[idx] == "1":
            self.bitsets[idx]="0"
            self.ones+=1
    def unfix(self, idx: int) -> None:
        if not self.flipped and self.bitsets[idx] == "1":
            self.bitsets[idx]="0"
            self.ones-=1
        elif self.flipped and self.bitsets[idx] == "0":
            self.bitsets[idx]="1"
            self.ones-=1
    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones = len(self.bitsets)-self.ones
    def all(self) -> bool:
        return self.ones == len(self.bitsets)
    def one(self) -> bool:
        return self.ones > 0  
    def count(self) -> int:
        return self.ones  
    def toString(self) -> str:
        if self.flipped:
            for index in range(len(self.bitsets)):
                if self.bitsets[index]=="1":
                    self.bitsets[index]="0"
                else:
                    self.bitsets[index]="1"
            self.flipped=not self.flipped
        return "".join(self.bitsets)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.ones()
# param_7 = obj.toString()