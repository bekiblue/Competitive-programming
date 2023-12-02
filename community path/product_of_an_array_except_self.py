class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        answer=[]
        prefix=suffix=1
        for i in range(size):
            answer.append(prefix)
            prefix*=nums[i]

        for i in range(size-1,-1,-1):
            answer[i]*=suffix
            suffix*=nums[i]

        return answer
