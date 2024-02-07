class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum=[]
        running_sum=0
        for index in range(len(nums)):
            running_sum+=nums[index]
            self.prefix_sum.append(running_sum)
    def sumRange(self, left: int, right: int) -> int:

        return self.prefix_sum[right]-self.prefix_sum[left-1] if left!=0 else self.prefix_sum[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)