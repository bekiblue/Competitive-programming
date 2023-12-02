class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        left= 0
        prefix_sum = 0
        result = len(nums)+1
        for i in range(len(nums)):
            prefix_sum += nums[i]
            while prefix_sum >= target:
                result = min(result, i+1-left)
                prefix_sum -= nums[left]
                left+= 1
        
        return result if result != len(nums)+1 else 0

            
