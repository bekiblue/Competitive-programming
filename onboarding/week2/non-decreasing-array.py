class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        possible=True
        for index in range(len(nums)-1):
            if nums[index] > nums[index+1] and possible :
                if  index+2<len(nums) and nums[index] <= nums[index+2] or index+1==len(nums)-1 :
                    nums[index+1]=nums[index]
                elif index and nums[index-1] <= nums[index+1] or not index:
                    nums[index]=nums[index+1]
                else:
                    return False  
                possible=False
            if nums[index] > nums[index+1] and not possible:
                return False
        return True 