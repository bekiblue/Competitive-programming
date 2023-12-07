class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives=[]
        negatives=[]
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        answer=[0]*len(nums)
        for index in range(len(positives)):
            answer[2*index]=positives[index]
            answer[2*index+1]=negatives[index]
        return answer