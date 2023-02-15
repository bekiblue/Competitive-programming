class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score =left=run=0
        right = len(tokens) - 1
        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                run += 1
                left += 1
            elif run > 0:
                power += tokens[right]
                run -= 1
                right -= 1
            else:
                break
            score = max(score, run)
        return score
