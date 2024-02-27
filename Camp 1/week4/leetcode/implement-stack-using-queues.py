class MyStack:
    def __init__(self):
        self.queue1=deque()
        self.queue2=deque()
    def push(self, x: int) -> None:
        if self.queue1 or not self.queue2:
            self.queue1.append(x)
        else:
            self.queue2.append(x) 
    def pop(self) -> int:
        while self.queue1:
            val=self.queue1.popleft()
            if not self.queue1:
                return val
            self.queue2.append(val)
        while self.queue2:
            val=self.queue2.popleft()
            if not self.queue2: 
                return val
            self.queue1.append(val)
    def top(self) -> int:
        val=self.pop()
        if self.queue1 or not self.queue2:
            self.queue1.append(val)
        else:
            self.queue2.append(val)
        return val
    def empty(self) -> bool:
        return not (self.queue1 or self.queue2) 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()