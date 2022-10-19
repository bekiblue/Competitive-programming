class MyQueue:

    def __init__(self):
        self.queue_stack = []

    def push(self, x: int) -> None:
        self.queue_stack.append(x)

    def pop(self) -> int:
        return self.queue_stack.pop(0)
        
    def peek(self) -> int:
        return self.queue_stack[0]

    def empty(self) -> bool:
        if self.queue_stack:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
