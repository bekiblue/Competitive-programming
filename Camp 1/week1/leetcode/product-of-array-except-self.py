class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[1]
        running_product=1
        for index in range(len(nums)-1):
            running_product*=nums[index]
            answer.append(running_product)
        current_product=1
        for index in range(len(nums)-1,0,-1):
            current_product*=nums[index]
            answer[index-1]*=current_product
        return answer






