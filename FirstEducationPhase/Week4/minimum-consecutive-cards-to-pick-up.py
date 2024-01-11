class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        index={}
        left=0
        mnm=len(cards)+1
        for right in range(len(cards)):
            if cards[right] in index:
                left=index[cards[right]]
                mnm=min(mnm,right-left+1)
            index[cards[right]]=right
        return mnm if mnm<len(cards)+1 else -1
             