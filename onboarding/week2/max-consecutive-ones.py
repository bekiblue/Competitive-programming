class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=0
        mxm=0
        for right in range(len(nums)):
            if nums[right]==0:
                mxm=max(mxm,right-left)
                left=right+1
            if right==len(nums)-1 and nums[right]==1:
                mxm=max(mxm,right-left+1)
 
        return mxm