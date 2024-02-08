class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        running_sum=0
        for index,num in enumerate(nums):
            if running_sum == total -running_sum-num:
                return index 
            running_sum+=num
        return -1