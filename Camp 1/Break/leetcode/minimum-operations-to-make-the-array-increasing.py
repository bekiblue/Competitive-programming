class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        operations = 0  

        for index in range(len(nums)-1):

            if nums[index] >= nums[index+1]:
                operations += (nums[index]-nums[index+1]) + 1
                nums[index+1]=nums[index]+1 

        return operations

