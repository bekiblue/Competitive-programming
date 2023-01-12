class MyCircularDeque:

    def __init__(self, k: int):
        self.limit = k
        self.deque = []

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.deque.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.deque.append(value)
        return True


    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.deque.pop(0)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.deque.pop()
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.deque[0]

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return True if not self.deque else False

    def isFull(self) -> bool:
        return len(self.deque) == self.limit
