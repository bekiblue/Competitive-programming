class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pointer=0
        two_pointer=len(nums)-1    
        reader=0 
        while reader <= two_pointer :
            if nums[reader]==1:
                reader+=1
            elif nums[reader]==0:
                nums[zero_pointer],nums[reader]=nums[reader],nums[zero_pointer]
                zero_pointer+=1
                reader+=1
            else:
                nums[two_pointer],nums[reader]=nums[reader],nums[two_pointer]
                two_pointer-=1