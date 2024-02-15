class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        left,right=0,len(nums)-4
        mnm=float("inf")
        while right < len(nums):
            mnm=min(mnm,nums[right]-nums[left])
            left,right=left+1,right+1
        return mnm
            

            