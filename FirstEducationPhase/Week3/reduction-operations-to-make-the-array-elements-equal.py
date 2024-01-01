class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        prev=nums[0]
        count=0
        for index in range(1,len(nums)):
            if nums[index]!=prev:
                count+=index
                prev=nums[index]
        return count
            