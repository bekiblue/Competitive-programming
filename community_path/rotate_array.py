class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        second = k
        tempList = nums.copy()
        for i in range(len(nums)):
            second = second % len(nums)
            nums[second] = tempList[first]
            first += 1
            second +=1
        
