class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score=0
        value=max(nums)
        for index in range(k):
            score+=value
            value+=1
        return score
