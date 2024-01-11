class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sub_sum=0
        mnm=float("inf")
        left=0
        for right in range(len(nums)):
            sub_sum+=nums[right]
            while sub_sum >= target:
                mnm=min(mnm,right-left+1)
                sub_sum-=nums[left]
                left+=1
        return mnm if mnm<float("inf") else 0
            