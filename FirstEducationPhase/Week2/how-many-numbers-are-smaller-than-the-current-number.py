class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num=sorted(nums)
        index={}
        answer=[]
        for i in range(len(sorted_num)):
           if sorted_num[i] not in index:
            index[sorted_num[i]]=i
        for num in nums:
            answer.append(index[num])
        return answer
        
