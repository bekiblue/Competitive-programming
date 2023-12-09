class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for num in set(range(len(nums)+1))-set(nums):
           return num
