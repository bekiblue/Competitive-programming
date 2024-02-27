class RecentCounter:
    def __init__(self):
        self.requests=deque() # It holds requests within the last 3000 milliseconds
    def ping(self, t: int) -> int:
        self.requests.append(t)
        while t-self.requests[0] > 3000:
            self.requests.popleft()
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)