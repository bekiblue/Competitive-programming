class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        mxm=0
        for side in range(len(nums)-1,1,-1):
            if nums[side-2]+nums[side-1] > nums[side]:
                mxm=max(mxm,nums[side-2]+nums[side-1]+nums[side])
        return mxm