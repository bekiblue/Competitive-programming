class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_index={}
        for index,value in enumerate(nums):
            num_index[value]=index
        for operation in operations:
            nums[num_index[operation[0]]]=operation[1]
            num_index[operation[1]]=num_index[operation[0]]
            del num_index[operation[0]]
        return nums
