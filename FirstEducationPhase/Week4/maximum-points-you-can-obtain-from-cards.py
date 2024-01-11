class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # remove the smallest sum subarray(Complementary to the one i want) with length len(cardPoints)-k
        complement=0
        w=len(cardPoints)-k
        for c in range(w):
            complement+=cardPoints[c]
        mnm_complement=complement
        total=complement
        for card in range(w,len(cardPoints)):
            total+=cardPoints[card]
            complement+=(cardPoints[card]-cardPoints[card-w])
            if complement < mnm_complement:
                mnm_complement=complement
        return total-mnm_complement 

