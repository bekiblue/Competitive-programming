from collections import defaultdict
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive=timeToLive
        self.generated=defaultdict(lambda :-timeToLive)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.generated[tokenId]=currentTime
        
    def renew(self, tokenId: str, currentTime: int) -> None:
        if currentTime - self.generated[tokenId] < self.timeToLive:
           self.generated[tokenId]=currentTime
        elif self.generated[tokenId] > 0:
            del self.generated[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count=0
        for tokenId in self.generated:
            if currentTime - self.generated[tokenId] < self.timeToLive:
                count+=1      
        return count



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)