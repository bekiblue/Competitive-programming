class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mnm=0
        running_sum=0
        mxm=float("-inf")       
        for num in nums:
            running_sum+=num
            mxm=max(mxm,running_sum-mnm)
            mnm=min(mnm,running_sum)
        return mxm