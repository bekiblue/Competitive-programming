class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        size=len(nums)
        prefix_sum=list(accumulate(nums))
        for i in range(size):
            if prefix_sum[i]-nums[i] == prefix_sum[size-1]-prefix_sum[i]:
                return i
        return -1
