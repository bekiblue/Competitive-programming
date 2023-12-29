class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for left in range(len(nums)):
            for right in range(left+1,len(nums)):
                if str(nums[right])+str(nums[left]) > str(nums[left])+str(nums[right]):
                    nums[left],nums[right]=nums[right],nums[left]
        answer=""
        prev=nums[0]
        zero=False if nums[0] else True
        for num in nums:
            if num!=prev:
                zero=False
            answer+=str(num)
        return "0" if zero else answer

