class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:  
        total=0
        for index in range(k):
            total+=nums[index]
        mxm=total
        for index in range(k,len(nums)):
            total=total-nums[index-k]+nums[index]
            mxm=max(mxm,total)
        return mxm/k