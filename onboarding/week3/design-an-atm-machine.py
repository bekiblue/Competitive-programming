class ATM:

    def __init__(self):
        self.notes=[0]*5
        self.dollar={0:20,1:50,2:100,3:200,4:500}
    def deposit(self, banknotesCount: List[int]) -> None:
        self.notes=[self.notes[index]+banknotesCount[index] for index in range(5)]
    def withdraw(self, amount: int) -> List[int]:
        original=self.notes.copy()
        paid=[0]*5 
        note_index=4
        while note_index >= 0 and amount >= 5:
            if self.dollar[note_index] <= amount and self.notes[note_index] > 0:
                n = min(amount//self.dollar[note_index],self.notes[note_index])
                paid[note_index]+=n
                amount -= n*self.dollar[note_index]
                self.notes[note_index]-=n
            else:
                note_index-=1
        if amount == 0:
            return paid
        else:
            self.notes=original
            return [-1]
        
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)