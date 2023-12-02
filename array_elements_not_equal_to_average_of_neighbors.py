class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)-1):
            prev = nums[i-1]
            nxt = nums[i+1]
            curr = nums[i]
            if (prev<curr and nxt>curr) or (prev>curr and nxt<curr):
                nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums
