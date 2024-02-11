class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        suffix=[0]*len(nums)
        running_sum=0
        for index in range(len(nums)-1,-1,-1):
            suffix[index]=running_sum
            running_sum+=nums[index]
        answer=[]
        prefix=[]
        running_sum=0
        for index,num in enumerate(nums):
            prefix.append(running_sum)
            running_sum+=num
            value=(index*nums[index]-(prefix[index]))+(suffix[index]-((len(nums)-index-1)*nums[index]))
            answer.append(value) 
        return answer


