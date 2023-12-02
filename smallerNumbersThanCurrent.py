class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in range(0,len(nums)):
            count=0
            for j in range(0,len(nums)):
                if i  != j and nums[i] > nums[j] : 
                    count += 1
            answer.append(count)
        return answer 
