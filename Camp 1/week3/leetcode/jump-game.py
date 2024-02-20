class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index=len(nums)-1
        for index in range(len(nums)-1,-1,-1):
            if index+nums[index] >= last_index:
                last_index=index
        return last_index==0 

