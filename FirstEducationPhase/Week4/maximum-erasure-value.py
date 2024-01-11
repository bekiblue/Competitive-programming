class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        index={}
        left=0
        max_score=0
        score=0
        for right in range(len(nums)):
            score+=nums[right]
            while nums[right] in index:
                index.pop(nums[left])
                score-=nums[left]
                left+=1
            index[nums[right]]=right
            max_score=max(max_score,score)
        return max_score        