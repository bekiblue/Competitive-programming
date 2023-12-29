class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for sorted_index in range(len(nums)-1):
            for unsorted in range(sorted_index+1,0,-1):
                if nums[unsorted] < nums[unsorted-1]:
                    nums[unsorted],nums[unsorted-1]=nums[unsorted-1],nums[unsorted]
                else:
                    break
        
        