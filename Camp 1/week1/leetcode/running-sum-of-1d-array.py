class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum=[]
        current_running_sum=0
        for index in range(len(nums)):
            current_running_sum+=nums[index]
            running_sum.append(current_running_sum)
        return running_sum


