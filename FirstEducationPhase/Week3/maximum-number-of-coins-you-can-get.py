class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        bob=0 
        me=len(piles)-2
        my_coin=0
        while bob < me:
            my_coin+=piles[me]
            me-=2
            bob+=1
        return my_coin