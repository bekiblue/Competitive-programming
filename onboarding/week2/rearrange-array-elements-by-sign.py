class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives=[]
        negatives=[]
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        answer=[]
        for index in range(len(positives)):
            answer.append(positives[index])
            answer.append(negatives[index])
        return answer