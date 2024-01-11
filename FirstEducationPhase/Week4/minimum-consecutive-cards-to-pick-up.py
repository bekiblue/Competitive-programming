class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mnm=float("inf")
        index={}
        left=0
        for right in range(len(cards)):
            if cards[right] in index and index[cards[right]] >= left:
                left=index[cards[right]]
                mnm=min(mnm,right-left+1)
            index[cards[right]]=right
        return mnm if mnm<float("inf") else -1
            
        