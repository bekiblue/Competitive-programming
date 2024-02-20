class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        answer=0
        for side in range(len(nums)-1,1,-1):
            if nums[side-1]+nums[side-2] > nums[side]:
                answer=nums[side]+nums[side-1]+nums[side-2]
                break
        return answer


